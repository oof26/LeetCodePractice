# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        left, right = 0, len(nums)-1
        index = len(nums)-1
        while(left<=right):
            if( abs(nums[left]) < abs(nums[right]) ):
                result[index] = nums[right]*nums[right]
                right-=1
            else:
                result[index] = nums[left]*nums[left]
                left+=1
            index-=1
        return result
                