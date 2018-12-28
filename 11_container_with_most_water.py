class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l = 0
        r = len(height)-1
        while l < r:
            num1 = height[l]
            num2 = height[r]
            max_area = max(max_area, min(num1, num2) * (r - l))
            if num1 < num2:
                l += 1
            else:
                r -= 1
        return max_area
