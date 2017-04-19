# -*- coding: utf-8 -*-
class Solution(object):
    def removeElement(self, nums, val):
        subIndex = 0
        for num in nums:
            if num != val:
                nums[subIndex] = num
                subIndex += 1
        return subIndex