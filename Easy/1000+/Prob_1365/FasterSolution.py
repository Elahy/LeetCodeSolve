class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp, hashmap, res = sorted(nums), {}, []
        for i in range(len(temp)):
            if i == 0:
                hashmap[temp[i]] = 0
            elif temp[i] == temp[i-1]:
                continue
            else:
                hashmap[temp[i]] = i
        for num in nums:
            res.append(hashmap[num])
        return res