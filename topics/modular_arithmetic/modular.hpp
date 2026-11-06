// GNU C++17; signed 64-bit inputs, 1 <= m <= LLONG_MAX.
// __int128 intermediates avoid signed overflow.
namespace modular {
using i64 = long long;
using i128 = __int128_t;
i64 norm(i128 a, i64 m) {
  a %= m; return i64(a < 0 ? a+m : a);
}
i64 add(i64 a, i64 b, i64 m) {
  return norm(i128(a)+b, m);
}
i64 sub(i64 a, i64 b, i64 m) {
  return norm(i128(a)-b, m);
}
i64 mul(i64 a, i64 b, i64 m) {
  return norm(i128(a)*b, m);
}
i64 power(i64 a, unsigned long long e, i64 m) {
  i64 r = 1 % m; a = norm(a, m);
  for (; e; e >>= 1, a = mul(a,a,m))
    if (e & 1) r = mul(r,a,m);
  return r; // O(log e); includes e=0 and m=1
}
// Inverse for ANY modulus > 1, iff gcd(a,m)==1.
optional<i64> inverse(i64 a, i64 m) {
  if (m <= 1) return nullopt;
  i64 r = m, s = norm(a,m); i128 x = 0, y = 1;
  while (s) {
    i64 q = r/s, t = r%s; r = s; s = t;
    i128 z = x-i128(q)*y; x = y; y = z;
  }
  if (r != 1) return nullopt;
  return norm(x,m); // O(log m)
}
// a*x == b (mod m). Return {x0, step}: all solutions
// x=x0+k*step; gcd(a,m) distinct residues modulo m.
optional<pair<i64,i64>> linear(i64 a, i64 b, i64 m) {
  a = norm(a,m); b = norm(b,m);
  i64 g = gcd(a,m);
  if (b % g) return nullopt;
  i64 step = m/g;
  if (step == 1) return pair<i64,i64>{0,1};
  return pair<i64,i64>{mul(b/g,*inverse(a/g,step),step),
                      step};
}
} // namespace modular
