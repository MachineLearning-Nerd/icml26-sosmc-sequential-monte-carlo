# SOSMC audit status

## Conservative verdict

- Overall status: INCONCLUSIVE
- Finite or special-case diagnostics: 5/5
- Scoped evidence points: 10/12
- Paper claims independently verified: 0/6
- Complete paper reproduction: false
- Current score claim: false
- Publication allowed: false
- Scientific runner executed by the standardization pass: false

## Claim statuses

| Claim | Status |
|---|---|
| C1 | FINITE_CONSISTENCY_PROXY |
| C2 | CONDITIONAL_EXACT_CERTIFICATE |
| C3 | CONDITIONAL_EXACT_CERTIFICATE |
| C4 | FINITE_VARIANCE_REDUCTION_PROXY |
| C5 | FINITE_TRACKING_PROXY |
| C6 | NOT_REPRODUCED |

The source verdict is outputs/verdict.json. The generated gate is
publication_gate.json. C2 and C3 remain selected-case certificates, and C6
remains an explicit negative for the absent MNIST EBM experiment.

## Scope boundary

The standardization pass changed documentation and metadata only. It did not
rerun the NumPy verifier, unit checks, author code, EBM training, ImpDiff
comparison, or MNIST experiment.
