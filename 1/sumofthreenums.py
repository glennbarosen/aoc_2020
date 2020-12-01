def threeNumsSums2020(numlist, sum):
    for num in numlist:
        for n in numlist:
            if (num + n < sum):
                for j in numlist:
                    if (num + n + j == sum):
                        return num, n, j, num * n * j


f = open("nums.txt", "r")
numbers = list(map(int, f.read().split()))
print(threeNumsSums2020(numbers, 2020))