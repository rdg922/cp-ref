const ll MOD = 1e9 + 7;

vvlong multMat(vvlong const &a, vvlong const &b) {
  int n = sz(a);
  vvlong ans = vvint(n, vint(n));
  rep(i, 0, n) {
    rep(j, 0, n) {
      rep(k, 0, n) { ans[i][j] += (a[i][k] * b[k][j]) % MOD; }
      ans[i][j] %= MOD;
    }
  }
  return ans;
}

vvlong matrixExpo(vvlong const &base, ll n) {
  if (n == 1) {
    return base;
  }

  vvlong matrix = matrixExpo(base, n / 2);
  if (n % 2 == 0) {
    return multMat(matrix, matrix);
  } else {
    return multMat(multMat(matrix, matrix), base);
  }
}

