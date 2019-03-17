class Solution:
    def bitwiseComplement(self, N: int) -> int:
        b = "{:b}".format(N)
        res = ""
        for i in range(len(b)):
            res += '0' if b[i] == '1' else '1'
        return int(res, 2)
