class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range (n):
            num1 = nums[i]
            num2 = target - num1       
            for j in range(i+1, n):
                if (nums[j] == num2):
                    return ([i,j])
                
if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())    
    sol = Solution()
    print(sol.twoSum(nums, target))