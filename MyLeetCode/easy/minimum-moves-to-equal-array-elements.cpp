#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minMoves(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int min = nums[0];

        int answer = 0;
        for (int i=1; i<nums.size(); i++) {
          answer += (nums[i]-min);
        }

        return answer;
    }
};

int main(void) {
  Solution sol;

  vector<int> nums;
  nums.push_back(1);
  nums.push_back(3);
  nums.push_back(2);

  int answer = sol.minMoves(nums);
  cout << answer << endl;
  return 0;
}
