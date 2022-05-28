class Solution:
    def digitCount(self, num: str) -> bool:
        checker = {}
        for i in num:
            if i in checker:
                checker[i] += 1
            else:
                checker[i] = 1
        for i in range(len(num)):
            if str(i) not in checker:
                checker[str(i)] = 0
            if not int(num[i]) == checker[str(i)]:
                return False
        return True