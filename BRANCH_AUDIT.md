# Branch and attribution audit

## Repository transition

- Legacy repository: icml26-repro-hCIBCAS1Hi-sosmc
- Canonical repository: icml26-sosmc-sequential-monte-carlo
- Source tip before this documentation pass:
  a6a000412a96b934a686eb4ffb9817377d3a5860
- Legacy repository's historical master tip:
  c1498f92aacb23827587c81215a67b3355385afa
- Pre-edit recovery bundle:
  /tmp/icml26-sosmc-before-history.bP5pNw/icml26-sosmc-before-history.bundle
- Recovery bundle SHA-256:
  787560583c07af451bc933e7ec8667f54fbde4b97c6f96409ceb3972d2d4e34a

The old repository used master as its default branch. The canonical published
repository uses main, and the old branch is not published.

## Canonical state

- Canonical branch: main
- Published branch count: one
- Final main tip: recorded in the collection inventory after publication
- Expected reachable identity:

~~~text
MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>
~~~

The prior numeric noreply address was replaced. No Claude co-author trailer
is permitted in the canonical history.

## Verification contract

The final verifier checks:

1. the exact documentation and gate files are present;
2. local and remote branch views contain only main;
3. all reachable author and committer identities use the canonical name and
   email;
4. the claim ledger agrees with outputs/verdict.json;
5. the conservative gate keeps publication_allowed false.
