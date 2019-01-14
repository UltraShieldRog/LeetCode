class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {}
        dic[2] = ['a', 'b', 'c']
        dic[3] = ['d', 'e', 'f']
        dic[4] = ['g', 'h', 'i']
        dic[5] = ['j', 'k', 'l']
        dic[6] = ['m', 'n', 'o']
        dic[7] = ['p', 'q', 'r', 's']
        dic[8] = ['t', 'u', 'v']
        dic[9] = ['w', 'x', 'y', 'z']
        
        res = []
        i = len(digits) - 1
        while i >= 0:
            if i == len(digits) - 1:
                res = dic[int(digits[i])].copy()
                i -= 1
                continue
            length = len(dic[int(digits[i])])
            res *= length
            current = 0
            stage = 1
            for letter in dic[int(digits[i])]:
                while current < len(res)//length*stage:
                    res[current] = letter + res[current]
                    current += 1
                stage += 1
            i -= 1
        return res
