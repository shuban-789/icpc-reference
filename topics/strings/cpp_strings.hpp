// std::string stores bytes; positions/lengths use size_t.
void string_calls() {
  string s = "abc", t(3, 'x');
  s += t; s.push_back('!'); s.pop_back();
  char c = s[0]; s[0] = 'A'; // at(i) checks bounds
  string part = s.substr(1, 3); // start, count
  s.insert(1, "yz"); s.erase(1, 2); // start, count
  s.replace(0, 1, "a"); // start, count, replacement
  size_t p = s.find("xx"); // string::npos if absent
  if (p != string::npos) part = s.substr(p);
  p = s.rfind('x'); // last match
  p = s.find_first_of("aeiou"); // any listed byte
  p = s.find_first_not_of(' '); // skip leading spaces
  bool same = (s == t), less = (s < t); // lexicographic
  bool prefix = s.compare(0, t.size(), t) == 0;
  reverse(s.begin(), s.end());
  sort(s.begin(), s.end());
  int count_x = count(s.begin(), s.end(), 'x');
  string digits = to_string(-123);
  size_t used;
  long long value = stoll("7f", &used, 16); // 127
  // stoi/stoll/stod throw on invalid/out-of-range input.
  // They may parse a prefix; check used==input.size().
  istringstream in("10 20"); int a, b; in >> a >> b;
  istringstream csv("a,b,c"); string field;
  while (getline(csv, field, ',')) { /* use field */ }
  c = char(tolower(static_cast<unsigned char>(c)));
  (void)p; (void)same; (void)less; (void)prefix;
  (void)count_x; (void)value;
}
// cin >> s reads a token; getline(cin,s) reads a line.
// After >>: cin.ignore(numeric_limits<streamsize>::max(),
// '\n'); then getline. getline(cin >> ws,s) also discards
// leading whitespace/blank lines (only if that is wanted).
