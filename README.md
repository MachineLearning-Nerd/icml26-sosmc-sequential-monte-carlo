# ICML 2026 — Efficient Stochastic Optimisation via Sequential Monte Carlo

Independent evidence audit for *Efficient Stochastic Optimisation via
Sequential Monte Carlo* by James Cuin, Davide Carbone, Yanbo Tang, and
O. Deniz Akyildiz.

- Repository: https://github.com/MachineLearning-Nerd/icml26-sosmc-sequential-monte-carlo
- Legacy repository: icml26-repro-hCIBCAS1Hi-sosmc
- Paper audit pin: https://arxiv.org/abs/2601.22003v1
- Latest paper record: https://arxiv.org/abs/2601.22003
- HTML paper: https://arxiv.org/html/2601.22003
- OpenReview: https://openreview.net/forum?id=hCIBCAS1Hi
- Official author code: https://github.com/akyildiz-group/SOSMC
- Collection anchor: hCIBCAS1Hi

This is an independent audit, not the authors' implementation. It preserves
the existing finite and special-case evidence and documents exactly where it
stops.

## Current result

| Boundary | Result |
|---|---:|
| Finite or special-case diagnostics | 5/5 pass |
| Scoped evidence points | 10/12 supported |
| Paper-level claims independently verified | 0/6 |
| Complete paper reproduction | false |
| Current score claim | false |
| publication_allowed | false |
| Overall status | INCONCLUSIVE |

C2 and C3 are conditional exact certificates for selected assumptions, not
verification of the general propositions. C6 is an explicit negative because
the required MNIST EBM campaign is absent. Every paper_claim_verified field is
false.

The standardization pass did not invoke repro/src/verify.py,
repro/tests/test_sosmc.py, the author code, or any scientific runner. The
committed outputs/verify_run.log and outputs/verdict.json are retained as
historical evidence.

## What the paper does

The paper studies optimization problems whose gradients are expectations over
parameter-dependent, intractable distributions. SOSMC treats successive
optimization targets as an SMC path, reuses particles, updates incremental
weights, and resamples when effective sample size is low. It analyzes
idealized convergence and ESS behavior and reports Langevin and
energy-based-model experiments, including MNIST.

## Claim-to-evidence ledger

| ID | Paper statement | Evidence production path | Status | Boundary |
|---|---|---|---|---|
| C1 | Algorithm 1 and Lemma 1: the weighted particle gradient estimator is consistent. | repro/src/verify.py → outputs/verdict.json:claims.c1 | FINITE_CONSISTENCY_PROXY | Direct samples from one known Gaussian are not general SMC propagation, weighting, and resampling |
| C2 | Proposition 2: the idealized update has the PL/smooth linear rate. | repro/src/verify.py → outputs/verdict.json:claims.c2 | CONDITIONAL_EXACT_CERTIFICATE | Selected anisotropic quadratic and negative controls do not prove the general proposition |
| C3 | Equation 19 and Propositions 3–4: ESS has the Gaussian identity and general small-step behavior. | repro/src/verify.py → outputs/verdict.json:claims.c3 | CONDITIONAL_EXACT_CERTIFICATE | Equal-covariance Gaussian identities and one quartic grid do not establish the general asymptotic result |
| C4 | Section 5: SOSMC reduces variance and improves relevant baselines. | repro/src/verify.py → outputs/verdict.json:claims.c4 | FINITE_VARIANCE_REDUCTION_PROXY | The comparison is a synthetic ULA proxy, not full EBM or ImpDiff training |
| C5 | Particle estimates track the true gradient during the optimization trajectory. | repro/src/verify.py → outputs/verdict.json:claims.c5 | FINITE_TRACKING_PROXY | One closed-form Gaussian/quadratic trajectory does not establish the general claim |
| C6 | Section 5.3: SOSMC remains robust on MNIST under kernel mismatch. | repro/src/verify.py → outputs/verdict.json:claims.c6 | NOT_REPRODUCED | No MNIST EBM pretraining, kernel-mismatch, or reward-tuning run is present |

## How each claim is produced

~~~text
historical finite inputs and selected exact identities
  -> repro/src/verify.py
       c1-c5 finite/special-case evidence
       c6 explicit missing-experiment record
  -> outputs/verdict.json
       authoritative six-claim evidence record
  -> repro/src/finalize_gate.py
       metadata-only status, count, and manifest validation
  -> outputs/gate.json and publication_gate.json
       conservative documentation gate
  -> verify_final.py
       repository, branch, identity, and documentation checks
~~~

A passing gate means that the scoped evidence labels are internally
consistent. It does not turn selected certificates into general theorem
verification or claim that the paper experiments were reproduced.

## Repository map

- repro/src/verify.py — original bounded scientific evidence producer.
- repro/tests/test_sosmc.py — independent identity and rate checks retained
  from the source repository.
- outputs/verdict.json — authoritative six-claim result.
- outputs/verify_run.log — historical bounded-run log.
- outputs/gate.json — generated structural gate result.
- publication_gate.json — root-level gate summary.
- .trackio/logbook — synchronized historical experiment notes.
- CLAIM_EVIDENCE.md — claim-to-evidence contract.
- SOURCE_AUDIT.md — source, version, and recovery boundary.
- ENVIRONMENT.md — execution and dependency boundary.
- EVIDENCE_MANIFEST.json — scoped evidence inventory.
- claims.json and reproduction_verdicts.json — machine-readable summaries.
- REPORT.md — standardized audit report.
- verify_final.py — dependency-light final-state verifier.

## Branch and attribution policy

The canonical repository is icml26-sosmc-sequential-monte-carlo and the
canonical branch is main; it is the sole published branch. The former
repository name and old master state are documented in BRANCH_AUDIT.md.

Reachable commits are normalized to:

~~~text
MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>
~~~

This attribution identifies collection-maintenance commits. It does not
claim authorship of the paper or the original scientific ideas.

## Citation

~~~bibtex
@article{cuin2026efficient,
  title = {Efficient Stochastic Optimisation via Sequential Monte Carlo},
  author = {Cuin, James and Carbone, Davide and Tang, Yanbo and Akyildiz, O. Deniz},
  journal = {arXiv preprint arXiv:2601.22003},
  year = {2026},
  doi = {10.48550/arXiv.2601.22003}
}
~~~

The machine-readable citation is in CITATION.cff.

## Thank you

Thank you to James Cuin, Davide Carbone, Yanbo Tang, and O. Deniz Akyildiz
for developing and sharing this clear SMC perspective on optimization with
intractable gradients. This independent audit is intended for learning and
evidence tracking, not as an official reproduction or endorsement.

## License and attribution

The repository-level audit code is maintained by MachineLearning-Nerd. The
paper, official code, terminology, figures, and scientific claims remain the
authors' work. Consult the paper and upstream repository for their licensing
terms.
