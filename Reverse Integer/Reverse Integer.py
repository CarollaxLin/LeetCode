# -*- coding: utf-8 -*-
class Solution(object):
    def reverse(self, x):
        rvInt = int(str(abs(x))[::-1])
        if x >= 0:
            return rvInt * (rvInt <= 0x7FFFFFFF)
        else:
            return -rvInt * (-rvInt >= -0x7FFFFFFF)