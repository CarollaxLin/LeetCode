# -*- coding: utf-8 -*-
class Solution(object):
    def countAndSay(self, n):
        num = '1'
        for i in range(n-1):
            count = 0
            temp = num[0]
            res = ''
            for char in num:
                if temp == char:
                    count += 1
                else:
                    res = res + str(count) + temp
                    temp = char
                    count = 1
            res = res + str(count) + temp
            num = res
        return num