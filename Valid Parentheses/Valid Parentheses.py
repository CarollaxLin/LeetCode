# -*- coding: utf-8 -*-

class Solution(object):
    def isValid(self, s):
        #  Use some simple checks which avoid the general rule to speed up
        if (s[0] in [')', ']', '}']) or (s[-1] in ['(', '[', '{']) or (len(s)%2 != 0):
            return False
        # General rule
        # Since first element has been checked, ignore it to speed up slightly.
        myDict = {'(':')', '[':']', '{':'}'}
        stack = [s[0]]
        for i in s[1:]:
            # Left parenthese case:
            # It can appear at any place and wait a right one to offset. Just append to the stack.
            if i in myDict:
                stack.append(i)
            # Right parenthese case:
            # The last element of the stack should be a left one and offset each other
            else:
                if stack == []:
                    return False
                elif i != myDict[stack.pop()]:
                    return False
        # Check if every parenthese was offset
        return stack == []