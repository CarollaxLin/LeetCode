# -*- coding: utf-8 -*-
# Brute-force method
class Solution1(object):
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return i+1

# Sandwich method
class Solution2(object):
    def searchInsert(self, nums, target):
        if (not nums) or (nums[0] > target):
            return 0
        elif nums[-1] < target:
            return len(nums)
        start = 0
        end = len(nums) - 1
        check = ((end - start)//2 + start)
        while end != start:
            if nums[check] > target:
                end = check
                check = ((end - start)//2 + start)
            elif nums[check] < target:
                start = check
                check = (end - (end - start)//2)
            else:
                return check
            if (nums[start] < target < nums[end]) & (end - start == 1):
                return end
        return check