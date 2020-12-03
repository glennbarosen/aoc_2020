def isValidPassword(p, minmax, letter):
    if int(minmax[0]) <= p.count(letter) <= int(minmax[1]):
        return True
    return False


f = open("passwords.txt", "r")
passwords_and_rules = f.read().split("\n")

p = []
count = 0

for i in passwords_and_rules:
    p.append(i.split(": "))

for i in p:
    password = i[1]
    minmax = i[0][0:-2].split("-")
    letter = i[0][-1:]
    if isValidPassword(password, minmax, letter):
        count += 1
print(count)
