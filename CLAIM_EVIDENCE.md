# Claim-to-evidence contract

This ledger maps each paper statement to the producer and committed output.
Finite or conditional statuses describe bounded evidence only. Every
paper_claim_verified field remains false.

| ID | Paper statement | Producer and output | Status | Boundary |
|---|---|---|---|---|
| C1 | Algorithm 1 and Lemma 1: the weighted particle gradient estimator is consistent. | repro/src/verify.py → outputs/verdict.json:claims.c1 | FINITE_CONSISTENCY_PROXY | One known Gaussian with direct samples is not general SMC |
| C2 | Proposition 2: the idealized update has the PL/smooth linear rate. | repro/src/verify.py → outputs/verdict.json:claims.c2 | CONDITIONAL_EXACT_CERTIFICATE | Selected quadratic assumptions do not prove the general proposition |
| C3 | Equation 19 and Propositions 3–4: ESS has the Gaussian identity and general small-step behavior. | repro/src/verify.py → outputs/verdict.json:claims.c3 | CONDITIONAL_EXACT_CERTIFICATE | Selected Gaussian identities and one quartic grid do not establish general asymptotics |
| C4 | Section 5: SOSMC reduces variance and improves relevant baselines. | repro/src/verify.py → outputs/verdict.json:claims.c4 | FINITE_VARIANCE_REDUCTION_PROXY | Synthetic ULA comparison is not full EBM or ImpDiff training |
| C5 | Particle estimates track the true gradient during optimization. | repro/src/verify.py → outputs/verdict.json:claims.c5 | FINITE_TRACKING_PROXY | One closed-form trajectory does not establish the general claim |
| C6 | Section 5.3: SOSMC remains robust on MNIST under kernel mismatch. | repro/src/verify.py → outputs/verdict.json:claims.c6 | NOT_REPRODUCED | No MNIST EBM pretraining, mismatch, or reward-tuning run is present |

## How each claim is produced

~~~text
historical bounded inputs
  -> repro/src/verify.py
       c1-c5 finite or conditional evidence
       c6 explicit missing-experiment record
  -> outputs/verdict.json
       authoritative source verdict
  -> repro/src/finalize_gate.py
       metadata-only status, count, and manifest checks
  -> outputs/gate.json and publication_gate.json
       conservative gate
  -> verify_final.py
       final repository-state audit
~~~

The standardization pass did not execute the scientific producer. Existing
outputs are retained as historical evidence. Conditional exact certificates
are not general theorem verification, and the C6 negative is not a score.
