import functools
class Solution:
    # Sample solution by user badgergo  
    def numDupDigitsAtMostN(self, N: int) -> int:
        digits = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if N <= 10:
            return 0
        str_N = list(map(int, str(N + 1)))
        n = len(str_N)
        ans = 0
        # for i in range(1, n + 1):
        #     ans += functools.reduce(operator.mul, digits[:i])
        used = set()
        A = [[1] * 10 for i in range(10)]
        for i in range(1, 10):
            for j in range(i):
                A[i][j + 1] = A[i][j] * (i - j)
        for i in range(1, n):
            ans += 9 * A[9][i - 1]
        n = len(str_N)
        for i, d in enumerate(str_N):
            start = 0 if i > 0 else 1
            for x in range(start, d):
                if x not in used:
                    ans += A[9 - i][n - i - 1]
            if d in used:
                break
            used.add(d)
        return N - ans
