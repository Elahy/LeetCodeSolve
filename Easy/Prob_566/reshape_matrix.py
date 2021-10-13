class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if(len(mat)*len(mat[0]) != r*c):
            return mat
        else:
            result = []
            temp = []
            i = 0
            l = 0
            while i < len(mat):
                j = 0
                while j < len(mat[0]):
                    temp.append(mat[i][j])
                    l += 1
                    if ( l == c):
                        result.append(temp)
                        temp = []
                        l = 0
                    j += 1
                i += 1
            return result