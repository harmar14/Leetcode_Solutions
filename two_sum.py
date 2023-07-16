nums = list(map(int, input().split()))
target = int(input())

n = len(nums)
for i in range (n):
    num1 = nums[i]
    num2 = target - num1       
    for j in range(i+1, n):
        if (nums[j] == num2):
            print([i,j])