class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            temp = "".join(sorted(word))
            if temp in anagram:
                anagram[temp].append(word)
            else:
                anagram[temp] = [word]
        res = []
        for key,val in anagram.items():
            res.append(val)
        return res
        