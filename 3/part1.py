f = open("map.txt", "r")
map = f.read().split("\n")
xpos = 0
trees = 0
count = 0

bigMap = []

for i in map:
    bigMap.append(i + i + i + i + i + i + i + i + i + i + i + i + i + i + i +
                  i + i + i + i + i + i + i + i + i + i + i + i + i + i + i +
                  i + i + i + i + i + i + i + i + i + i + i + i + i + i + i +
                  i + i + i + i + i + i + i + i + i + i + i + i + i + i + i +
                  i + i + i + i + i + i + i + i + i + i + i + i + i + i + i +
                  i + i + i + i + i + i + i + i + i + i + i + i + i + i + i +
                  i + i + i + i + i + i + i + i + i + i + i + i + i + i + i +
                  i + i + i + i + i + i + i + i + i + i + i + i + i + i + i +
                  i + i + i + i + i + i + i + i)

for i in bigMap:
    if i[xpos] == "#":
        trees += 1
    xpos += 3
    count += 1
    print(trees)
