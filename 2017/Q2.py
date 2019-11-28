#Name: Zacchary Dempsey-Plante
#Date: 2017-02-22
#Question: Shifty Sum

num = int(input())
shiftCount = int(input())
total = num

for i in range(shiftCount):
    total += num * pow(10, i + 1)

print(total)
