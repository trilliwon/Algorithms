#include <bits/stdc++.h>
// https://www.hackerrank.com/challenges/strong-password/problem

using namespace std;

int minimumNumber(int n, string password) {

    bool hasDigit = false;
    bool hasLower = false;
    bool hasUpper = false;
    bool hasSpecial = false;

    for (int i=0; i<password.length(); i++) {
        if (isupper(password[i])) {
            hasUpper = true;
        } else if (islower(password[i])) {
            hasLower = true;
        } else if (isdigit(password[i])) {
            hasDigit = true;
        } else {
            hasSpecial = true;
        }
    }
    
    int neededCondCount = 4 - (hasDigit + hasLower + hasUpper + hasSpecial);    
    int pwLength = password.length();

    if ((pwLength - 6) >= 0) {
        return neededCondCount;
    } else {
        return (6 - pwLength) > neededCondCount ? (6 - pwLength) : neededCondCount;
    }
}

int main() {
    int n;
    cin >> n;
    string password;
    cin >> password;
    int answer = minimumNumber(n, password);
    cout << answer << endl;
    return 0;
}

