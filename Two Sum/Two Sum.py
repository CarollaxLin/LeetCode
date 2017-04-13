# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            if ((target - num) in nums):
                if (nums.index(target - num) != i):
                    return sorted([i, nums.index(target - num)])