class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True
        if len(s) != len(t):
            result = False
        else:
            i = 0
            dict = {}
            while i<len(s):
                if s[i] in dict:
                    i += 1
                elif s[i] in t:
                    if s.count(s[i]) == t.count(s[i]):
                        dict.update({s[i] : "1"})
                        i += 1
                    else:
                        result = False
                        break
                else:
                    result = False
                    break
        return result
        