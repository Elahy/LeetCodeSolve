class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for wealth in accounts:
            richest = max(richest, sum(wealth))
        return richest
        