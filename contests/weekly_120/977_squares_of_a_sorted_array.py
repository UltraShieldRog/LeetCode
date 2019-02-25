class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = list(map(lambda x: x ** 2, A))
        res.sort()
        return res
