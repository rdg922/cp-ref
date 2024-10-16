vlong fact(3e5);

ll MOD = 1e9 + 7;

fact[0] = 1;
rep(i, 1, sz(fact)) fact[i] = (i * fact[i - 1]) % MOD;

ll C(int n, int k) {
  if (k > n)
    return 0;
  return ((fact[n] * inverse_mod(fact[k]) % MOD * inverse_mod(fact[n - k])) % MOD;
}

ll inv_mod(int n) { return b_exp(n, MOD - 2); }
