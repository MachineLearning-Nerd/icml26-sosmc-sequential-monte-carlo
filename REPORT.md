# SOSMC audit report

## Executive result

The repository is a clean, conservative audit of selected finite and
special-case consequences. It is not a complete reproduction of the SOSMC
paper.

| Measure | Result |
|---|---:|
| Overall status | INCONCLUSIVE |
| Finite or special-case diagnostics | 5/5 |
| Evidence points | 10/12 |
| Paper claims verified | 0/6 |
| Complete paper reproduction | false |
| Current score claim | false |
| Publication allowed | false |

## Claim outcomes

- C1: FINITE_CONSISTENCY_PROXY
- C2: CONDITIONAL_EXACT_CERTIFICATE
- C3: CONDITIONAL_EXACT_CERTIFICATE
- C4: FINITE_VARIANCE_REDUCTION_PROXY
- C5: FINITE_TRACKING_PROXY
- C6: NOT_REPRODUCED

C2 and C3 are useful selected-case certificates. C6 is an explicit negative
for the missing MNIST EBM campaign. The full claim paths and limitations are
in CLAIM_EVIDENCE.md.

## Scope

Included evidence covers a known-Gaussian Monte Carlo gradient proxy,
selected quadratic and ESS identities, finite variance and tracking
diagnostics, and the explicit absence of the MNIST experiment.

Excluded evidence covers general SMC propagation and resampling, complete
theorem proofs, full EBM and ImpDiff comparisons, 2D EBM benchmarks, and
MNIST training and kernel mismatch.

## Repository state

The canonical repository is
MachineLearning-Nerd/icml26-sosmc-sequential-monte-carlo with one published
branch named main. The branch transition and history recovery details are in
BRANCH_AUDIT.md.
