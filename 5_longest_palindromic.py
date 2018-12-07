def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """

    # deal with odd length palindrome
    def find_p_odd(s, sub_index):
        i = 1
        res = s[sub_index]
        if sub_index-i < 0 or sub_index+i == len(s):
            return res
        while s[sub_index-i] == s[sub_index+i]:
            res = s[sub_index-i] + res + s[sub_index+i]
            i += 1
            if sub_index-i < 0 or sub_index+i == len(s):
                return res

        return res

    # deal with even length palindrome
    def find_p_even(s, sub_index):
        i = 1
        res = ''
        if sub_index+i == len(s):
            return res
        if sub_index-i < 0 :
            if s[sub_index] == s[sub_index+1]:
                return s[sub_index] + s[sub_index+1]
            else:
                return res
        if s[sub_index] == s[sub_index+1]:
            res += s[sub_index:sub_index+2]
        else:
            return res
        if sub_index+1+i == len(s):
            return res
        while s[sub_index-i] == s[sub_index+1+i]:
            res = s[sub_index-i] + res + s[sub_index+1+i]
            i += 1
            if sub_index-i < 0 or sub_index+1+i == len(s):
                return res
        return res

    palindrome = []
    i = 0
    while i < len(s):
        temp1 = find_p_odd(s,i)
        temp2 = find_p_even(s,i)
        if len(temp1) > 0:
            palindrome.append(temp1)
        if len(temp2) > 0:
            palindrome.append(temp2)
        i += 1

    if len(palindrome) == 0:
        return ''

    palindrome.sort(key= lambda lst: len(lst))
    return palindrome[-1]
