#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
       for i in range(len(nums)):
           for j in (i+1,range(len(nums))):
               if nums[i] + nums[j] == target:
                   return i,j




if __name__ == '__main__':
    a = Solution()
    nums = [1,2,3,4]
    target = 3
    print a.twoSum(nums,target)