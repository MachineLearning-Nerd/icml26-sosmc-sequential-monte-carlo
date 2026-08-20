# Source and version audit

## Paper identity

- Title: Efficient Stochastic Optimisation via Sequential Monte Carlo
- Authors: James Cuin; Davide Carbone; Yanbo Tang; O. Deniz Akyildiz
- Audit pin: arXiv 2601.22003v1
- Latest record: arXiv 2601.22003v2
- OpenReview: hCIBCAS1Hi
- Official code: https://github.com/akyildiz-group/SOSMC

## Repository source boundary

The repository contains a CPU-oriented finite and special-case audit:
repro/src/verify.py, repro/tests/test_sosmc.py, outputs/verdict.json,
outputs/verify_run.log, and the synchronized .trackio/logbook.

The repository does not contain a general SMC propagation/resampling campaign,
full EBM or ImpDiff comparison, 2D EBM benchmark, or MNIST kernel-mismatch
campaign. C6 is therefore an honest NOT_REPRODUCED result.

The standardization pass added documentation, machine-readable summaries, and
metadata gates. It did not run the verifier, tests, author code, or training.
outputs/verdict.json remains the authoritative evidence record.

## Pre-edit recovery

The source tip before this pass was:

~~~text
a6a000412a96b934a686eb4ffb9817377d3a5860
~~~

The recovery bundle is:

~~~text
/tmp/icml26-sosmc-before-history.bP5pNw/icml26-sosmc-before-history.bundle
~~~

Its SHA-256 is:

~~~text
787560583c07af451bc933e7ec8667f54fbde4b97c6f96409ceb3972d2d4e34a
~~~

## Attribution

Reachable commits are normalized to:

~~~text
MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>
~~~

This is collection-maintenance attribution, not paper authorship.
