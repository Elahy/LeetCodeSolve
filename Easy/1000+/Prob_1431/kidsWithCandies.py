class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        great = max(candies)
        array = [False]*len(candies)
        for i in  range(len(candies)):
            if candies[i]+extraCandies >= great:
                array[i] = True
        return array
        