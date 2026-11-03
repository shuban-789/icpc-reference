#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

template <typename... T>
void in(T&... args) {
    (cin >> ... >> args);
}

template <typename... T>
void print(const T&... args) {
    (cout << ... << args);
}

template <typename... T>
void println(const T&... args) {
    (cout << ... << args) << '\n';
}

template <typename... T>
void flintln(const T&... args) {
    (cout << ... << args) << endl;
}

template <typename... T>
void dbg(const T&... args) {
    (cout << "DEBUG: " << ... << args) << '\n';
}

template <typename T>
string format_vec(const vector<T>& vec) {
    ostringstream oss;
    oss << "[";
    for (size_t i = 0; i < vec.size(); ++i) {
        oss << vec[i];
        if (i != vec.size() - 1) {
            oss << ", ";
        }
    }
    oss << "]";
    return oss.str();
}

void solve() {
    // solution
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    solve();
}