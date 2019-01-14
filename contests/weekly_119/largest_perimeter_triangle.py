class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        
        p1 = len(A)-3
        p2 = len(A)-2
        p3 = len(A)-1
        while A[p1] + A[p2] <= A[p3]:
            p1 -= 1
            p2 -= 1
            p3 -= 1
            if p3 < 2:
                return 0
        return A[p1] + A[p2] + A[p3]

# Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

# If it is impossible to form any triangle of non-zero area, return 0.


# Example 1:

# Input: [2,1,2]
# Output: 5
# Example 2:

# Input: [1,2,1]
# Output: 0
# Example 3:

# Input: [3,2,3,4]
# Output: 10
# Example 4:

# Input: [3,6,2,3]
# Output: 8
