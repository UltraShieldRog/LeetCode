class Solution:
    def isValid(self, S: str) -> bool:
        # a good sample solution
        if not S:
            return True
        f = S.find('abc')
        if f == -1:
            return False
        return self.isValid(S[:f] + S[f + 3:])

        # my own method
        # length = len(S)
        # if length % 3 != 0:
        #     return False
        # lst = [char for char in S]
        # exist = True
        # while exist:
        #     exist = False
        #     i = 0
        #     while i < len(lst)-2:
        #         if lst[i:i+3] == ["a", "b", "c"]:
        #             exist = True
        #             lst[i], lst[i+1], lst[i+2] = '0', '0', '0'
        #         i += 1
        #     while '0' in lst:
        #         lst.remove('0')
        # if len(lst) == 0:
        #     return True
        # return False
