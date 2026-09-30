# Claim level: point versus complete analysis

For a request for an **opinion**, a point on, or a review of **already received
quotes**, provide the useful, source-backed finding on the verified subset.
Label it `partial_review`, state that it is not an exhaustive consultation
analysis, and list:

- every opened quote with its exact project-relative path;
- every enumerated but unreadable or unreviewed candidate with its path and
  reason; and
- the folders or source families still required for a complete analysis.

For a request explicitly seeking a **complete**, **global** or **all-quotes**
analysis, first establish the candidate set and read every material document.
If that condition is not met, do not give an overall conformity conclusion.
Return the verified partial findings as useful context, identify the exact
missing paths or families, and ask whether the user wants to: (a) stop pending
the missing sources, or (b) continue with an explicitly limited analysis. Use
`needs_user_input` when that choice changes the requested conclusion; otherwise
use `ready_with_limits`.
