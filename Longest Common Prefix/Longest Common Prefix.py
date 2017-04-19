# -*- coding: utf-8 -*-
# Application of zip
class Solution1(object):
    def longestCommonPrefix(self, strs):
        zipped = zip(*strs)
        res = ""
        for i in zipped:
            if len(set(i)) == 1:
                res = res + i[0]
            else:
                return res
        return res
    
# Another method
class Solution2(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for index, element in enumerate(shortest):
            for s in strs:
                if s[index] != element:
                    return shortest[:index]
        return shortest