// C++17; use with the contest template. Ranges are [l,r).
void container_calls() {
  vector<int> v(3, 0); // size 3, initialized to zero
  v.reserve(10); // capacity only; size unchanged
  v.resize(5, 2); v.push_back(7); v.emplace_back(8);
  v.pop_back(); // requires nonempty; returns void
  v.insert(v.begin()+1, 9); v.erase(v.begin()+1);
  v.erase(remove(v.begin(), v.end(), 2), v.end());
  int x = v[0]; // unchecked; v.at(i) checks bounds
  x = v.front(); x = v.back();
  for (int& y : v) ++y; // reference to mutate
  array<int, 4> a{}; a.fill(3); // fixed size
  deque<int> d; d.push_front(x); d.push_back(x);
  d.pop_front(); d.pop_back(); // ends: O(1)
  stack<int> st; st.push(x); x = st.top(); st.pop();
  queue<int> q; q.push(x); x = q.front(); q.pop();
  priority_queue<int> hi; // largest first
  priority_queue<int, vector<int>, greater<int>> lo;
  hi.push(x); x = hi.top(); hi.pop();
  lo.push(x); x = lo.top(); lo.pop();
  set<int> s{1, 3}; // sorted unique keys
  auto [it, inserted] = s.insert(2);
  it = s.find(3); // end() if absent
  if (it != s.end()) s.erase(it);
  it = s.lower_bound(2); // first >= 2
  it = s.upper_bound(2); // first > 2
  if (it != s.begin()) x = *prev(it); // predecessor
  multiset<int> ms{2, 2, 3};
  ms.erase(ms.find(2)); // one copy; must exist
  ms.erase(2); // ALL copies of key 2
  map<string, int> mp; // sorted unique keys
  ++mp["key"]; // inserts zero if key absent
  mp.emplace("other", 4); // won't replace existing
  mp.insert_or_assign("other", 5); // set/replace
  auto jt = mp.find("key"); // lookup, no insertion
  if (jt != mp.end()) x = jt->second;
  for (auto& [key, value] : mp) ++value;
  mp.erase("key"); // returns number erased
  unordered_map<int, int> um;
  um.max_load_factor(0.7f); um.reserve(100);
  um[x] = 1; // hash table; no sorted order/bounds
  unordered_set<int> us; us.insert(x);
  bitset<64> bits(5); // fixed number of bits
  bits.set(1); bits.reset(2); bits.flip(0);
  bool b = bits.test(1); auto n = bits.count();
  b = bits.any(); b = bits.none(); b = (bits.all)();
  // Parentheses avoid the template's all(x) macro.
  bits <<= 2; bits |= bitset<64>(3);
  auto mask = bits.to_ullong(); // throws if too large
  v.clear(); // size=0; capacity may remain
  (void)a; (void)inserted; (void)b; (void)n; (void)mask;
}
