class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        diff = [c[0] - c[1] for c in costs]
        indexes = sorted(range(0, N), key=lambda x: diff[x])
        
        result = 0
        for i in range(N//2):
            result += costs[indexes[i]][0]
            result += costs[indexes[N-i-1]][1]
        return result
