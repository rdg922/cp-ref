ll b_exp(ll a, ll b) {
  if (b == 0 or a == 1)
    return 1;
  return ((ll)(b % 2 == 1 ? a : 1) * (ll)expo((a * a) % MOD, b / 2)) % MOD;
}
