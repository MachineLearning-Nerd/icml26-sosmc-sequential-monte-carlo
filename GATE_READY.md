# Documentation gate

This repository is ready to publish as an honest scoped audit, not as a full
reproduction of the SOSMC paper.

## Gate decision

- Overall status: INCONCLUSIVE
- Finite or special-case diagnostics: 5/5 pass
- Scoped evidence points: 10/12 supported
- Paper claims independently verified: 0/6
- Complete paper reproduction: false
- Current score claim: false
- Publication allowed: false
- Gate status: PASS for the stated audit scope

Expected claim statuses:

- C1 FINITE_CONSISTENCY_PROXY
- C2 CONDITIONAL_EXACT_CERTIFICATE
- C3 CONDITIONAL_EXACT_CERTIFICATE
- C4 FINITE_VARIANCE_REDUCTION_PROXY
- C5 FINITE_TRACKING_PROXY
- C6 NOT_REPRODUCED

Run repro/src/finalize_gate.py only when intentionally checking metadata.
The standardization pass did not run the scientific verifier or tests.
