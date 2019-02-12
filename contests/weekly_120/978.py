class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        if len(A) == 2:
            if A[0] != A[1]:
                return 2
            else:
                return 1
        max = 1   
        while True:
            temp_max = 1 
            if len(A) == 0 or len(A) == 1:
                break
            x = 0
            y = 1
            
            if A[x] > A[y]:
                while A[x] > A[y]:
                    temp_max += 1
                    x += 1
                    y += 1
                    x, y = y, x
                    if x == len(A) or y == len(A):
                        break
                A = A[temp_max-1:]
            elif A[x] < A[y]:
                while A[x] < A[y]:
                    temp_max += 1
                    x += 1
                    y += 1
                    x, y = y, x
                    if x == len(A) or y == len(A):
                        break
                A = A[temp_max-1:]
            else:
                A = A[1:]
            max = temp_max if temp_max > max else max
        return max
