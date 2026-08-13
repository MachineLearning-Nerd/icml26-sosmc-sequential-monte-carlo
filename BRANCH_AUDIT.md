# Branch and attribution audit

## Historical state

Before normalization, the repository was:

- Name: icml26-repro-hCIBCAS1Hi-sosmc
- Remote: MachineLearning-Nerd/icml26-repro-hCIBCAS1Hi-sosmc
- Default branch: master
- Historical master tip: c1498f92aacb23827587c81215a67b3355385afa
- Branches observed: master only

The historical commit used loop-sosmc / loop@local and included a Claude
co-author trailer. That attribution and the overclaiming root message are not
retained in the normalized published history.

## Canonical state

- Repository: MachineLearning-Nerd/icml26-sosmc-sequential-monte-carlo
- Canonical branch: main
- Legacy master branch: removed after main was published
- Expected branch count: one

All reachable published commits are normalized to:

~~~text
MachineLearning-Nerd
37579156+MachineLearning-Nerd@users.noreply.github.com
~~~

No Claude co-author trailer is permitted in the canonical history.

## Verification checklist

The final publication check must confirm:

1. GitHub metadata uses the canonical repository name and main as default.
2. The only remote branch is main.
3. The main tip contains README.md, STATUS.md, GATE_READY.md,
   BRANCH_AUDIT.md, the canonical verdict, and the publication gate.
4. Paginated commit attribution reports MachineLearning-Nerd for every
   reachable commit.
5. No reachable commit contains the old Claude co-author trailer.
