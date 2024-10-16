ll compute_hash(const string &s) {
  int p = 31;
  ll hash_value = 0;
  ll p_pow = 1;
  for (char c : s) {
    hash_value = (hash_value + (c - 'a' + 1) * p_pow) % MOD;
    p_pow = (p_pow * p) % MOD;
  }
  return hash_value;
}

int suffixCount(std::string S, int L) {
  string suffix = S.substr(sz(S) - L, sz(S));
  ll problem = compute_hash(suffix);

  string substring = S.substr(0, L);
  ll start = compute_hash(substring);

  ll count = 0;
  if (start == problem)
    count++;

  rep(i, L, sz(S)) {
    start -= (S[i - L] - 'a' + 1);
    start = start * inv_mod(31) % MOD;
    start += (S[i] - 'a' + 1) * (ll)pow(31, L - 1) % MOD;

    if (start == problem)
      count++;
  }
  return count;
}
