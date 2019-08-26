class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> ans;
        vector<int> pcount(26, 0);
        vector<int> scount(26, 0);

        for (int i=0; i<p.length(); i++) {
            scount['z' - s[i]] += 1;
            pcount['z' - p[i]] += 1;
        }

        bool isequal = true;

        for (int i=0; i<26; i++) {
            if (scount[i] != pcount[i]) {
                isequal = false;
                break;
            }
        }

        if (isequal) {
            ans.push_back(0);
        }

        int firstIndex = 0;

        for (int i = p.length(); i<s.length(); i++) {
            scount['z' - s[firstIndex++]] -= 1;
            scount['z' - s[i]] += 1;

            bool isequal = true;

            for (int j = 0; j<26; j++) {
                if (scount[j] != pcount[j]) {
                    isequal = false;
                    break;
                }
            }

            if (isequal) {
                ans.push_back(firstIndex);
            }
        }
        return ans;
    }
};
