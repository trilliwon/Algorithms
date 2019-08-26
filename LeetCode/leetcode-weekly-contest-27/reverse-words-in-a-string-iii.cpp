#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
      string word;
      string reversed;
      int insert_pos = 0;
      int j = 0;
      for (int i=0; i<s.length(); i++) {
        if (s[i] != ' ') {
          word.insert(j++, 1, s[i]);
        } else {
          word = reverseWord(word);
          reversed.insert(insert_pos, word);
          insert_pos += word.length();
          reversed.insert(reversed.end(), ' ');
          insert_pos++;
          j = 0;
          word = "";
        }
      }
      reversed.insert(insert_pos, reverseWord(word));
      return reversed;
    }

    string reverseWord(string word) {
      int begin = 0;
      int end = word.length()-1;
      for (int k=0; k<word.length()/2; k++) {
        char temp = word[begin];
        word[begin] = word[end];
        word[end] = temp;
        begin++;
        end--;
      }
      return word;
    }
};
