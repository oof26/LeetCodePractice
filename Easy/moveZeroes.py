# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0
        
        for x in range(0,len(nums)):
            if (nums[x] != 0):
                nums[lastNonZero]=nums[x]
                lastNonZero+=1
        
        for y in range(lastNonZero,len(nums)):
            nums[y]=0