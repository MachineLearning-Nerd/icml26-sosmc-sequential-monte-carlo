# Verification run

The latest bounded run was:

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 repro/src/verify.py
python3 repro/src/finalize_gate.py
~~~

Result:

~~~text
FINITE PROXIES: 5/5
PAPER CLAIMS VERIFIED: 0/6
OVERALL: INCONCLUSIVE
~~~

The verifier uses the fixed seed in repro/src/verify.py and writes
outputs/verdict.json. The publication gate is standard-library-only and
validates the six expected statuses.
