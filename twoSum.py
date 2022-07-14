class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i,num in enumerate(nums):
            if target - num in dict:
                return ([dict[target - num],i])
            elif num not in dict:
                dict[num] = i