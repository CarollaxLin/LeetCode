# -*- coding: utf-8 -*-
class Solution(object):
    def romanToInt(self, s):
        romanDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # Look up dict directly for one char case would slightly speed up.
        if len(s) == 1:
            return romanDict[s]
        # General rule
        else:
            res = romanDict[s[-1]]
            for i in range(len(s)-1):
                if romanDict[s[-i-1]] > romanDict[s[-i-2]]:
                    res -= romanDict[s[-i-2]]
                else:
                    res += romanDict[s[-i-2]]
            return res