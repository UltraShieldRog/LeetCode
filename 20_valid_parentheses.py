from collections import deque
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def match(s1, s2):
            if s1 == '(':
                if s2 == ')':
                    return True
                return False
            elif s1 =='[':
                if s2 == ']':
                    return True
                return False
            elif s1 =='{':
                if s2 == '}':
                    return True
                return False
            
        d = deque()
        for char in s:
            if char in '([{':
                d.append(char)
            else:
                if len(d) != 0:
                    temp = d.pop()
                else:
                    return False
                if not match(temp, char):
                    return False
        if len(d) == 0:
            return True
        else:
            return False

