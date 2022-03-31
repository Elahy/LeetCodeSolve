class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        i = len(cost)-1
        cost.sort()
        res = 0
        while(i > 0):
            res += cost[i] + cost[i-1]
            i -= 3
        if i == 0: return res+cost[0]
        return res