class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def check(s1,s2):
            for i in s1:
                if i in s2:
                    return False
            return True
        
        result = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if check(words[i],words[j]) == True:
                    result = max(result,len(words[i])*len(words[j]))
                
        return result