def twoNumSumsTo2020(numlist, sum):
    for num in numlist:
        for n in numlist:
            if (num + n == sum):
                return [num, n], num * n


f = open("nums.txt", "r")
numbers = list(map(int, f.read().split()))
print(twoNumSumsTo2020(numbers, 2020))