class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        num = 0
        count = 0
        i = len(A) -1
        while i >= 0:
            num += A[i] * (10 ** count)
            count += 1
            i -= 1
        sum = num + K
        print(sum)
        res = [int(digit) for digit in str(sum)]
        return res
