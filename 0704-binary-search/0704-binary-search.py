class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
        if target == nums[0]:
            return 0
        if target == nums[right]:
            return right
        if target < nums[0] or target > nums[right]:
            return -1
        while left < right-1:
            center = int((left + right)/2)
            if target == nums[center]:
                return center
            elif target < nums[center]:
                right = center
            elif target > nums[center]:
                left = center
        return -1