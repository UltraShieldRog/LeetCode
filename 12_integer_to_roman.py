class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        d4 = num//1000
        d3 = (num - d4*1000)//100
        d2 = (num - d4*1000 - d3*100)//10
        d1 = (num - d4*1000 - d3*100 - d2*10)
        
        res += 'M'* (d4)
        
        def generate_str(digit, c1, c2, c3):
            res = ''
            if 0 <= digit <= 3:
                res += c1 * digit
            elif 4 <= digit <= 8:
                if digit == 4:
                    res += c1
                    res += c2
                else:
                    res += c2
                    res += c1 * (digit - 5)
            else:
                res += c3
            return res
        
        res += generate_str(d3, 'C', 'D', 'CM')
        res += generate_str(d2, 'X', 'L', 'XC')
        res += generate_str(d1, 'I', 'V', 'IX')
        
        return res
