#include <bits/stdc++.h>

// https://www.hackerrank.com/challenges/camelcase/problem

using namespace std;

int camelcase(string s) {
    int count = 1;
    for (int i=0; i<s.length(); i++) {
        if (isupper(s[i])) count++;
    }
    return count;
}

int main() {
    string s;
    cin >> s;
    int result = camelcase(s);
    cout << result << endl;
    return 0;
}

