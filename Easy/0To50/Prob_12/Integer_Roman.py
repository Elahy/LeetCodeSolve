class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        if num >= 1000:
            m = (num // 1000)
            ans += "M" * m
            num -= m*1000
            
        if num >= 900:
            ans += "CM"
            num -= 900
        elif num >= 500:
            c = (num - 500) // 100
            if c >= 1:
                ans += "D"
                ans += "C"*c
                num -= (500 + 100*c)
            else:
                ans += "D"
                num -= 500
        elif num >= 400:
            ans += "CD"
            num -= 400
        elif num >= 100:
            c = num // 100
            ans += "C"*c
            num -= 100*c
            
        if num >= 90:
            ans += "XC"
            num -= 90
        elif num >= 50:
            l = (num - 50) // 10
            if l >= 1:
                ans += "L"
                ans += "X"*l
                num -= (50 + 10*l)
            else:
                ans += "L"
                num -= 50
        elif num >= 40:
            ans += "XL"
            num -= 40
        elif num >= 10:
            x = num // 10
            ans += "X"*x
            num -= 10*x
            
        if num == 9:
            ans += "IX"
            num -= 9
        elif num >= 5:
            v = num - 5
            if v >= 1:
                ans += "V"
                ans += "I"*v
                num -= (5 + v)
            else:
                ans += "V"
                num -= 5
        elif num >= 4:
            ans += "IV"
            num -= 4
        elif num >= 1:
            ans += "I"*num
            num = 0
            
        if num == 0:
            return ans
        