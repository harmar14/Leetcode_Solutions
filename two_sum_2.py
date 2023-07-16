class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        isFound = False
        n = len(numbers)
        for i in range (n):
            num1 = numbers[i]
            num2 = target - num1
            left = i + 1
            right = n - 1
            center = (n - i + 1)//2
            while left <= right:
                center = (left + right) // 2
                if num2 == numbers[center]:
                    return([i+1,center+1])
                    break
                if num2 > numbers[center]:
                    left = center + 1
                else:
                    right = center - 1

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())    
    sol = Solution()
    print(sol.twoSum(nums, target))