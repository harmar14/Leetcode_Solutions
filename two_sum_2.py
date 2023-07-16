numbers = list(map(int, input().split()))
target = int(input())

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
            print([i+1,center+1])
            break
        if num2 > numbers[center]:
            left = center + 1
        else:
            right = center - 1