"""Independent unit tests for the SOSMC clean-room identities (hCIBCAS1Hi).

Run:  python -m pytest repro/tests/test_sosmc.py      (or: python repro/tests/test_sosmc.py)
These assert the same machine-precision identities the verifier relies on, via a
separate, minimal code path (no import of verify.py).
"""
import numpy as np


def test_equality_c3_gaussian_ess_identity():
    """ESS_inf/N = exp(-gamma^2 ||g||^2_{Sig^-1}) follows exactly from the
    equal-covariance Gaussian chi^2 = exp(gamma^2 ||g||^2) - 1."""
    Sig = np.diag([0.5, 1.0, 2.0, 0.25])
    Si = np.linalg.inv(Sig)
    g = np.array([1.5, -0.5, 1.0, -1.0])
    for gamma in [0.05, 0.1, 0.2, 0.4]:
        s2 = gamma ** 2 * (g @ Si @ g)
        chi2 = np.expm1(s2)                       # exp(s2)-1
        ess_over_N = 1.0 / (1.0 + chi2)
        assert abs(ess_over_N - np.exp(-s2)) < 1e-12


def test_equality_c2_pl_inequality_tight_in_lambda_min_mode():
    """PL assumption: l-l* <= (1/2mu)||grad l||^2, with equality in the lambda_min mode."""
    A = np.diag([1.0, 2.0, 5.0, 10.0])
    mu = 1.0
    w, V = np.linalg.eigh(A)
    th = 2.5 * V[:, 0]                            # lambda_min eigenvector
    lhs = 0.5 * th @ (A @ th)
    rhs = (1.0 / (2 * mu)) * np.sum((A @ th) ** 2)
    assert abs(lhs - rhs) / rhs < 1e-12           # equality
    # and the inequality holds for an off-mode point
    th2 = np.array([3.0, -2.0, 1.0, -3.0])
    assert (0.5 * th2 @ (A @ th2)) <= (1.0 / (2 * mu)) * np.sum((A @ th2) ** 2) + 1e-12


def test_c1_score_identity_unbiased():
    """E_{pi_theta}[ f(X) * Sigma^-1 (X-theta) ] = theta - x_*  (the exact grad)."""
    Sig = np.diag([0.5, 1.0, 2.0, 0.25]); Si = np.linalg.inv(Sig)
    x_star = np.array([1.0, -1.5, 0.5, 2.0])
    theta = np.array([2.0, 0.0, -1.0, 1.0])
    rng = np.random.default_rng(0)
    X = rng.multivariate_normal(theta, Sig, size=2_000_000)
    f = 0.5 * np.sum((X - x_star) ** 2, axis=1)
    g_hat = (f[:, None] * (X @ Si - theta @ Si)).mean(axis=0)
    assert np.linalg.norm(g_hat - (theta - x_star)) < 0.02


def test_c2_rate_bound_holds():
    """l(theta_k) <= (1-gamma mu)^k l(theta_0) for GD on a mu-PL/L-smooth quadratic."""
    A = np.diag([1.0, 2.0, 5.0, 10.0]); mu, L = 1.0, 10.0
    gamma = 1.0 / L; rho = 1 - gamma * mu
    th = np.array([3.0, -2.0, 1.0, -3.0]); f0 = 0.5 * th @ (A @ th)
    for k in range(40):
        assert (0.5 * th @ (A @ th)) <= (rho ** k) * f0 + 1e-10
        th = th - gamma * (A @ th)


if __name__ == "__main__":
    for fn in [test_equality_c3_gaussian_ess_identity,
               test_equality_c2_pl_inequality_tight_in_lambda_min_mode,
               test_c1_score_identity_unbiased,
               test_c2_rate_bound_holds]:
        fn(); print("PASS", fn.__name__)
    print("all tests passed")
