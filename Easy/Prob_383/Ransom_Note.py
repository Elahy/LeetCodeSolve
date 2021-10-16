class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        i = 1
        result = True
        while i <= len(ransomNote):
            if ransomNote[i-1:i] in dict:
                i += 1
            elif ransomNote[i-1:i] in magazine:
                if ransomNote.count(ransomNote[i-1:i]) <= magazine.count(ransomNote[i-1:i]):
                    dict.update({ransomNote[i-1:i] : "1"})
                    i += 1
                else:
                    result = False
                    break
            else:
                result = False
                break
        return result