def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    """
    # Method 1
    lst = nums1 + nums2
    lst.sort()
    if len(lst)%2 == 0:
        return (lst[len(lst)//2 - 1] + lst[len(lst)//2])/2
    else:
        return lst[len(lst)//2]
    """

    # Method 2: merge sort
    def merge(left, right):
        """Given two sorted lists, merge them into a single sorted list.

        Returns:
            The merged sorted list of left and right.
        """
        i = 0
        j = 0
        new_list = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                new_list.append(left[i])
                i += 1
            else:
                new_list.append(right[j])
                j += 1

        if i < len(left):
            for index in range(i,len(left)):
                new_list.append(left[index])
        if j < len(right):
            for index in range(j,len(right)):
                new_list.append(right[index])
        return new_list

    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst)//2
        lst1 = merge_sort(lst[:mid])
        lst2 = merge_sort(lst[mid:])
        return merge(lst1,lst2)

    res = merge_sort(nums1+nums2)
    return res[len(res)//2] if len(res)%2 != 0 else (res[len(res)//2 - 1] + res[len(res)//2])/2
