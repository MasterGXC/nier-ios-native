# Provenance and reference review

Reviewed 2026-10-27. References are not automatically merged: licenses, runtime
contracts and shader-chain compatibility must be checked for each change.

| Project | Role | License/revision evidence | Integration |
| --- | --- | --- | --- |
| [seedds/nxnative](https://github.com/seedds/nxnative) | Native host, graphics, iOS launcher, build system | MIT; current patch base in upstream.json | Actual base and attributed present allocator completion fix |
| [jhaizhou-ops/d2r-mobile](https://github.com/jhaizhou-ops/d2r-mobile) | Earlier native-host design and controller/resource ownership reference | MIT; historical source lineage | Design reference; not a separate NieR implementation |
| [LNPANDY/NX2Apple](https://github.com/LNPANDY/NX2Apple) | Windows build frontend, RomFS archive integration, launcher planning | LICENSE at 1f15ad608f26ac85abf8575fce447b137e9da0f2 grants MIT and retains jhaizhou/LNPANDY notices | Reviewed; no new source copied into this patch |

NX2Apple's 50d3671ec5b6b2a8e4a5c47c8cf293f3478ff093 explicitly clarifies
that the proposed launcher has not been built and the Windows package is withheld
pending hardware reports. Do not treat its runtime-profile foundation as a shipped
launcher or a verified solution to NieR scene performance.

The integrated experimental source preserves the existing shader chain. The
upstream present fix is 82ab25b40b75b3b7ce7e1da614ea15f231e8a029. The
geometry pool is local work, kept opt-in and documented with its performance cost.
The previously attempted aggressive 64 MiB general-arena cache trim was removed;
it caused allocation churn and is not recommended.

No unrelated game port, proprietary game binary, game-derived shader library or
private build history is merged here. A source integration is not a merger of
all referenced projects' ownership or a claim to their authorship.

The next candidate's launcher and settings model are from nxnative revision
`cdc6cef6b0250fcb54a061e4c55d56382b5d18ad`; local changes carry the earlier
Chinese strings into that UI without replacing its persistence/override rules.

[ThrecL's NieR follow-up PR #336](https://github.com/seedds/nxnative/pull/336)
was reviewed at `89ee0df21497070bfd3d826cc9d0184a82065b33`. It reports Mac
60 fps and variable iPhone performance (one heavy scene 39.13 fps). These are
author-reported observations, not this project's iPad acceptance. Its graphics
ABI changes require matching shader rebuilds; its dynamic-resolution sites are
gated to a different main build. No fixed addresses are transferred blindly.
