class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        
        for i, s in enumerate(s1):
            if s != s2[i]:
                return s1[:i]
        return s1
