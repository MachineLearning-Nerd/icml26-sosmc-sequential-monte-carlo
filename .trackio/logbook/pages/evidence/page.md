# Evidence

## Production path

~~~text
repro/src/verify.py
        |
        v
outputs/verdict.json
        |
        v
repro/src/finalize_gate.py
        |
        +--> outputs/gate.json
        +--> publication_gate.json
~~~

## Recorded result

~~~text
FINITE PROXIES: 5/5
PAPER CLAIMS VERIFIED: 0/6
OVERALL: INCONCLUSIVE
c6: NOT_REPRODUCED
~~~

The exact numerical evidence is kept in outputs/verdict.json. The finite
results are selected-instance checks and do not prove the general theorems or
application-level claims.
