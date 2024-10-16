set<int> pf(int n) {
  set<int> f;
  for (int i = 2; i * i <= n; i++)
    while (n % i == 0)
      f.insert(i), n /= i;
  if (n > 1)
    f.insert(n);
  return f;
}

vint factor(ll num) {
  vint facs;
  for (int div = 2; div * div < num; div++) {
    // OR loop through all primes
    while (num % div == 0) {
      num /= div;
      facs.pb(div);
    }
  }
  return facs;
}
