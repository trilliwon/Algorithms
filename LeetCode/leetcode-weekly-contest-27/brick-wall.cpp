#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <map>

using namespace std;

class Solution {
public:
    int leastBricks(vector<vector<int> >& wall) {
      map<int, int> result;
      int maxNC = 0;

      for (int i=0; i<wall.size(); i++) {
        int sum = 0;
        for (int j=0; j<wall[i].size()-1; j++) {
          sum += (wall[i][j]);
          result[sum] += 1;
          maxNC = max(maxNC, result[sum]);
        }
      }
      return wall.size() - maxNC;
    }
};

int main(void) {

  Solution sol;
  vector<vector<int> > wall;
/*
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
*/
  int innerArr1[] = {1, 2, 2, 1};
  vector<int> inner1 (innerArr1, innerArr1 + sizeof(innerArr1) / sizeof(int) );
  wall.push_back(inner1);

  int innerArr2[] = {3, 1, 2};
  vector<int> inner2 (innerArr2, innerArr2 + sizeof(innerArr2) / sizeof(int) );
  wall.push_back(inner2);

  int innerArr3[] = {1, 3, 2};
  vector<int> inner3 (innerArr3, innerArr3 + sizeof(innerArr3) / sizeof(int) );
  wall.push_back(inner3);

  int innerArr4[] = {2, 4};
  vector<int> inner4 (innerArr4, innerArr4 + sizeof(innerArr4) / sizeof(int) );
  wall.push_back(inner4);

  int innerArr5[] = {3, 1, 2};
  vector<int> inner5 (innerArr5, innerArr5 + sizeof(innerArr5) / sizeof(int) );
  wall.push_back(inner5);

  int innerArr6[] = {1, 3, 1, 1};
  vector<int> inner6 (innerArr6, innerArr6 + sizeof(innerArr6) / sizeof(int) );
  wall.push_back(inner6);

  int result = sol.leastBricks(wall);
  cout << result << endl;
  return 0;
}
