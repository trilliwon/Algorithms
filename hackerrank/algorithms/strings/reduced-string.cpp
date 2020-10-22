#include <iostream>
#include <string>
 
using namespace std;

string super_reduced_string(string s){
    bool removed = true;

    while(removed) {
        removed = false;

        for (int i=1; i<s.length(); i++) {
            if (s[i] == '0' && s[i-1] == '0') continue;
            if (s[i-1] == s[i]) {
                s[i-1] = s[i] = '0';
                removed = true;
            }
        }
        
        string temp = "";
        for (auto c : s) {
            if (c != '0') temp.push_back(c);
        }
        s = temp;
    }
    
    return s.length() == 0 ? "Empty String" : s;
}

int main() {
    string s;
    cin >> s;
    string result = super_reduced_string(s);
    cout << result << endl;
    return 0;
}
