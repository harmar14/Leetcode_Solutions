class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            center = (left + right) // 2
            if target == nums[center]:
                return center
                break
            if target > nums[center]:
                left = center + 1
            else:
                right = center - 1
        else:
            return -1
