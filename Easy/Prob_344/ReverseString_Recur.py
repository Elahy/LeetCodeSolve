class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recur(lo, hi):
            if hi <= lo:
                return
            s[lo], s[hi] = s[hi], s[lo]
            recur(lo+1, hi-1)
        recur(0, len(s)-1)