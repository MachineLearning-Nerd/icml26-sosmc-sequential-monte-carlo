# Publication gate

This repository is publication-ready as an **honest scoped audit**. It is
not marked as a full reproduction of the SOSMC paper.

## Gate decision

- Overall status: INCONCLUSIVE
- Finite or special-case diagnostics: 5/5 pass
- Paper claims independently verified: 0/6
- Full paper reproduction: false
- Gate: PASS for the stated audit scope

Expected claim statuses:

- C1 FINITE_CONSISTENCY_PROXY
- C2 CONDITIONAL_EXACT_CERTIFICATE
- C3 CONDITIONAL_EXACT_CERTIFICATE
- C4 FINITE_VARIANCE_REDUCTION_PROXY
- C5 FINITE_TRACKING_PROXY
- C6 NOT_REPRODUCED

Run:

~~~bash
python3 repro/src/finalize_gate.py
~~~

The gate validates outputs/verdict.json and writes outputs/gate.json and
publication_gate.json. A passing gate means that the finite evidence and
documentation agree; it does not prove the general theorems or experiments.
