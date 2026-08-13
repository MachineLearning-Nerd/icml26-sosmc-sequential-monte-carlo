# SOSMC — audit status

Paper: Efficient Stochastic Optimisation via Sequential Monte Carlo
Authors: James Cuin, Davide Carbone, Yanbo Tang, and O. Deniz Akyildiz
Reference: arXiv:2601.22003v1

## Conservative result

**Overall: INCONCLUSIVE**

- Bounded finite or special-case diagnostics passed: 5/5.
- Paper-level claims independently verified: 0/6.
- C6 MNIST EBM robustness: NOT_REPRODUCED.

The prior 5/6 VERIFIED label counted selected-instance calculations as
general paper verification. It is superseded by outputs/verdict.json.

| Claim | Current status |
| --- | --- |
| C1 consistency | FINITE_CONSISTENCY_PROXY |
| C2 PL convergence | CONDITIONAL_EXACT_CERTIFICATE |
| C3 ESS behavior | CONDITIONAL_EXACT_CERTIFICATE |
| C4 variance reduction | FINITE_VARIANCE_REDUCTION_PROXY |
| C5 gradient tracking | FINITE_TRACKING_PROXY |
| C6 MNIST robustness | NOT_REPRODUCED |

The missing general SMC algorithm, full EBM experiments, baselines, and MNIST
campaign are described in the README.
