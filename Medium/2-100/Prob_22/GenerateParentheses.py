class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(op,cl,temp):
            if len(temp) == n*2:
                res.append(temp)
                return
            if op<n:
                temp += "("
                backtrack(op+1,cl,temp)
                temp = temp[:-1]
            if cl<op:
                temp += ")"
                backtrack(op,cl+1,temp)
                temp = temp[:-1]
        res, temp = [], ""
        backtrack(0,0,temp)
        return res