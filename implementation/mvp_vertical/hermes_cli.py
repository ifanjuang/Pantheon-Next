"""One-shot operator CLI for the external Pantheon-Hermes execution bridge."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Iterable

from .hermes_distribution import DistributionLockError, validate
from .hermes_run_binding import (
    ExternalHermesRunBinding,
    HermesRunBindingError,
    HermesRunsHttpClient,
    PantheonRunBridgeClient,
)
from .hermes_runs_observer import HermesRunsApiObserver, HermesRunsObservationError


class HermesCliError(ValueError):
    pass


def _required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise HermesCliError(f"required environment variable is missing: {name}")
    return value


def _write_json(payload: dict[str, Any], output: Path | None) -> None:
    rendered = json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    if output is None:
        sys.stdout.write(rendered)
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")


def _load_receipt(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise HermesCliError(f"cannot read launch receipt {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise HermesCliError("launch receipt must be a JSON object")
    return value


def _observer(args: argparse.Namespace) -> HermesRunsApiObserver:
    return HermesRunsApiObserver(
        _required_env("HERMES_API_BASE"),
        _required_env("HERMES_API_KEY"),
        allowed_tools=args.allowed_tools,
        required_tools=args.required_tools,
        timeout=args.timeout,
    )


def _binding(args: argparse.Namespace) -> ExternalHermesRunBinding:
    observer = _observer(args)
    pantheon = PantheonRunBridgeClient(
        _required_env("PANTHEON_HERMES_API_BASE"),
        _required_env("PANTHEON_HERMES_API_KEY"),
        _required_env("PANTHEON_HERMES_ACTOR"),
        timeout=args.timeout,
    )
    hermes = HermesRunsHttpClient(
        _required_env("HERMES_API_BASE"),
        _required_env("HERMES_API_KEY"),
        timeout=args.timeout,
    )
    return ExternalHermesRunBinding(observer=observer, pantheon=pantheon, hermes=hermes)


def _add_runtime_args(parser: argparse.ArgumentParser, *, require_allowlist: bool) -> None:
    parser.add_argument(
        "--allowed-tool",
        action="append",
        dest="allowed_tools",
        required=require_allowlist,
        help="operator-reviewed Hermes tool name; repeatable",
    )
    parser.add_argument(
        "--required-tool",
        action="append",
        dest="required_tools",
        help="tool that must be active; repeatable and must be included in --allowed-tool",
    )
    parser.add_argument("--timeout", type=float, default=10.0)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pantheon-hermes",
        description=(
            "Execute one bounded Hermes bridge operation. This CLI has no daemon, "
            "scheduler, queue, polling loop or automatic retry."
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    verify = sub.add_parser(
        "verify-distribution",
        help="validate schema, paths, component digests and bounded routes",
    )
    verify.add_argument("--manifest", type=Path, required=True)
    verify.add_argument("--schema", type=Path, required=True)
    verify.add_argument("--mvp-root", type=Path, required=True)
    verify.add_argument("--next-root", type=Path, required=True)
    verify.add_argument("--output", type=Path)

    observe = sub.add_parser("observe", help="observe Hermes capabilities and toolsets once")
    _add_runtime_args(observe, require_allowlist=True)
    observe.add_argument("--output", type=Path)

    launch = sub.add_parser(
        "launch",
        help="qualify, reserve and submit one human-admitted read-only run",
    )
    _add_runtime_args(launch, require_allowlist=True)
    launch.add_argument("--admission-id", required=True)
    launch.add_argument("--idempotency-key", required=True)
    launch.add_argument("--output", type=Path)

    reconcile = sub.add_parser(
        "reconcile",
        help="observe one existing run once and record a terminal candidate when mappable",
    )
    _add_runtime_args(reconcile, require_allowlist=False)
    reconcile.add_argument("--receipt", type=Path, required=True)
    reconcile.add_argument("--idempotency-key", required=True)
    reconcile.add_argument("--output", type=Path)

    return parser


def execute(args: argparse.Namespace) -> dict[str, Any]:
    if args.command == "verify-distribution":
        roots = {
            "pantheon-mvp": args.mvp_root.resolve(),
            "Pantheon-Next": args.next_root.resolve(),
        }
        for name, root in roots.items():
            if not root.is_dir():
                raise HermesCliError(f"repository root does not exist: {name}={root}")
        return validate(
            manifest_path=args.manifest,
            schema_path=args.schema,
            repository_roots=roots,
        )

    if args.command == "observe":
        return _observer(args).observe()

    if args.command == "launch":
        admission_id = args.admission_id.strip()
        if not admission_id.startswith("admission-"):
            raise HermesCliError("--admission-id must be a Pantheon admission-... identity")
        return _binding(args).launch(
            admission_id=admission_id,
            idempotency_key=args.idempotency_key.strip(),
        )

    if args.command == "reconcile":
        return _binding(args).reconcile_once(
            launch_receipt=_load_receipt(args.receipt),
            idempotency_key=args.idempotency_key.strip(),
        )

    raise HermesCliError(f"unsupported command: {args.command}")


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        result = execute(args)
        _write_json(result, args.output)
    except (
        DistributionLockError,
        HermesCliError,
        HermesRunBindingError,
        HermesRunsObservationError,
        ModuleNotFoundError,
    ) as exc:
        print(f"pantheon-hermes refused: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
