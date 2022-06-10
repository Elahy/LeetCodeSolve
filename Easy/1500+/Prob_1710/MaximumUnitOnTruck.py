class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        dicto = {}
        for box,unit in boxTypes:
            if unit in dicto:
                dicto[unit] += box
            else:
                dicto[unit] = box
        res = 0
        for unit in sorted (dicto.keys(), reverse=True):
            print(unit, dicto[unit])
            if dicto[unit] < truckSize:
                res += dicto[unit]*unit
                truckSize -= dicto[unit]
            else:
                res += truckSize*unit
                break
        return res