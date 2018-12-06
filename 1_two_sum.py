def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    complement_dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in complement_dict:
            return [complement_dict[complement], i]
        else:
            if nums[i] in complement_dict:
                continue
            complement_dict[nums[i]] = i
