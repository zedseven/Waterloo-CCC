#Name: Zacchary Dempsey-Plante
#Date: 2017-02-22
#Question: Quadrant Selection

num0 = int(input()) #x
num1 = int(input()) #y
if num0 > 0:
    if num1 > 0: #x and y are positive
        print('1')
    elif num1 < 0: #x is positive, but y is negative
        print('4')
elif num0 < 0:
    if num1 > 0: #x is negative and y is positive
        print('2')
    elif num1 < 0: #x and y are negative
        print('3')
