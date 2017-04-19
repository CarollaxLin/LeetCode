# -*- coding: utf-8 -*-
# Use built-in function
class Solution1(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
        
# Brute-force method
class Solution2(object):
    def strStr(self, haystack, needle):
        match = 0
        index = 0
        while match < len(needle):
            if len(needle) > len(haystack[index:]):
                return -1
            match = 0
            for i in range(len(needle)):
                if needle[i] == haystack[index+i]:
                    match += 1
                    if match == len(needle):
                        break
                else:
                    index += 1
                    break
        return index

# A little improvement on brute-force method
class Solution3(object):
    def strStr(self, haystack, needle):
        match = 0
        index = 0
        while match < len(needle):
            if len(needle) > len(haystack[index:]):
                return -1
            match = 0
            search = True
            for i in range(len(needle)):
                if (haystack[index+i] == needle[0]) & (i != 0) & search:
                    nextIndex = index + i
                    search = False
                if needle[i] == haystack[index+i]:
                    match += 1
                    if match == len(needle):
                        break
                elif search:
                    index += (i+1)
                    break
                else:
                    index = nextIndex
                    break
        return index