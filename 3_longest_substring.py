def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """

    longest_sub = ''
    sub = ''

    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[j] in sub:
                break
            sub += s[j]
        if len(sub) > len(longest_sub):
            longest_sub = sub
        sub = ''

    return len(longest_sub)
