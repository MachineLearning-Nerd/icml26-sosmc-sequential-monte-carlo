# Efficient Stochastic Optimisation via Sequential Monte Carlo (SOSMC)

**OpenReview:** https://openreview.net/forum?id=hCIBCAS1Hi  ·  **arXiv:** https://arxiv.org/abs/2601.22033
**ICML 2026 · Probabilistic Methods · CPU-only clean-room reproduction**

Independent, from-first-principles verification of the paper's core mathematical
claims on a fully-specified synthetic instance. **No author code is used**; every
quantity is computed in numpy from the definitions in the paper.

## Result: 5 / 6 claims verified (10 pts)

| claim | statement | status |
|---|---|---|
| c1 | Algorithm 1 / Lemma 1 — the self-normalised particle gradient `ĝ=ΣwᵢH(xᵢ)` is a consistent estimator of `∇ℓ` (rate 1/√N; analytic `E[H]=∇ℓ`). | ✅ PASS |
| c2 | Prop 2 — μ-PL + L-smooth, γ≤1/L ⟹ `ℓ(θₖ)−ℓ* ≤ (1−γμ)ᵏ(ℓ(θ₀)−ℓ*)`. Bound holds (κ=10, zero violation); PL inequality tight to machine precision in the λ_min mode; negative controls (γ>2/L diverges; θ⁴ sub-linear). | ✅ PASS (machine precision) |
| c3 | Eq 19 + Props 3/4 — `ESS∞(γ)=N·exp(−γ²‖∇ℓ‖²_{Σ⁻¹})` for Gaussian targets (derived exactly from the equal-covariance χ²); general `χ²=γ²∇ℓᵀI_θ∇ℓ+O(γ³)` (χ²/γ²→I_θ, slope 2, numeric-Fisher cross-check). | ✅ PASS (machine precision) |
| c4 | Variance-reduction mechanism — particle-estimate variance ∝ 1/ESS (slope −1.04); SOSMC MSE ≪ single-chain SOUL at matched compute. *"Beats ImpDiff"* EBM benchmark out of scope (needs training). | ✅ PASS (mechanism) |
| c5 | Particle estimates track `∇ℓ(θₖ)` throughout optimization; outer loop converges at/below the Prop-2 linear rate (final sub-optimality 0.0035 ≪ bound 0.218). | ✅ PASS |
| c6 | MNIST EBM robustness under kernel mismatch. | ⛔ honest negative — needs EBM pretraining + Langevin reward tuning (GPU/training); not run under the CPU-only campaign. |

## The coherent instance

All five verified claims are exercised on **one** closed-form instance:

- `π_θ = 𝒩(θ, Σ)` (the Gaussian target of Eq 19)
- `f(x) = ½‖x − x_*‖²`
- `ℓ(θ) = E_{πθ}[f(X)] = ½‖θ − x_*‖² + ½tr(Σ)`  ⟹  `∇ℓ(θ) = θ − x_*` (μ-PL μ=1, L-smooth L=1)
- score-identity estimator `H_θ(x) = f(x)·Σ⁻¹(x − θ)` is **exactly unbiased** for `∇ℓ`.

A second anisotropic quadratic (κ=10) demonstrates Prop 2's bound for a non-trivial
condition number, and a 1-D quartic target demonstrates the general (Prop 3/4) χ².

## Run

```bash
cd papers/icml26-repro-hCIBCAS1Hi-sosmc
uv venv --python 3.12 .venv && .venv/bin/python -m pip -q install numpy
.venv/bin/python repro/src/verify.py        # writes outputs/verdict.json
.venv/bin/python repro/tests/test_sosmc.py  # 4 unit tests
```

Full evidence: `outputs/verdict.json`, `outputs/verify_run.log`, `.trackio/logbook/`.
