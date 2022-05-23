class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1, string2 = "", ""
        for part in word1:
            string1 += part
        for part in word2:
            string2 += part
        return string1 == string2