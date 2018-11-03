class Solution {
public:
    int leastBricks(vector<vector<int> >& wall) {
      map<int, int> result;
      int width = 0;
      for (int i=0; i<wall[0].size(); i++) {
        width += wall[0][i];
      }

      int sum = 0;
      int maxNC = 0;
      for (int i=0; i<wall.size(); i++) {
        for (int j=0; j<wall[i].size()-1; j++) {
          sum += (wall[i][j]);
          result[sum] += 1;
          maxNC = max(maxNC, result[sum]);
        }
        sum = 0;
      }

      return wall.size() - maxNC;
    }
};
