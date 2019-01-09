class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
                return 0
        if s[0] == 'I':
                if len(s) == 1:
                        return 1
                elif s[1] == 'V':
                        s = s[2:] if len(s) != 2 else ''
                        return 4 + self.romanToInt(s)
                elif s[1] == 'X':
                        s = s[2:] if len(s) != 2 else ''
                        return 9 + self.romanToInt(s)                                
                else:
                        s = s[1:] if len(s) != 1 else ''
                        return 1 + self.romanToInt(s) 
        elif s[0] == 'X':
                if len(s) == 1:
                        return 10
                elif s[1] == 'L':
                        s = s[2:] if len(s) != 2 else ''
                        return 40 + self.romanToInt(s)
                elif s[1] == 'C':
                        s = s[2:] if len(s) != 2 else ''
                        return 90 + self.romanToInt(s)                                
                else:
                        s = s[1:] if len(s) != 1 else ''
                        return 10 + self.romanToInt(s)
        elif s[0] == 'C':
                if len(s) == 1:
                        return 100
                elif s[1] == 'D':
                        s = s[2:] if len(s) != 2 else ''
                        return 400 + self.romanToInt(s)
                elif s[1] == 'M':
                        s = s[2:] if len(s) != 2 else ''
                        return 900 + self.romanToInt(s)                                
                else:
                        s = s[1:] if len(s) != 1 else ''
                        return 100 + self.romanToInt(s)
        elif s[0] == 'V':
                 s = s[1:] if len(s) != 1 else ''
                 return 5 + self.romanToInt(s)
        elif s[0] == 'L':
                 s = s[1:] if len(s) != 1 else ''
                 return 50 + self.romanToInt(s)
        elif s[0] == 'D':
                 s = s[1:] if len(s) != 1 else ''
                 return 500 + self.romanToInt(s)
        elif s[0] == 'M':
                 s = s[1:] if len(s) != 1 else ''
                 return 1000 + self.romanToInt(s)
        else:
                raise ValueError('Invalid Input')
