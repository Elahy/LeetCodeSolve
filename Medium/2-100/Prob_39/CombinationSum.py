class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def permute(arr,sums,lo):
            if sums > target: return
            if sums == target: res.append(arr)
            
            for hi in range(lo,len(candidates)):
                permute(arr+[candidates[hi]], sums+candidates[hi], hi)
        res, arr = [], []
        permute(arr, 0, 0)
        return res;