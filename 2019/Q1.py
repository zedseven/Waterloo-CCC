flipsStr = input()
h = 1
v = 1
for c in range(len(flipsStr)):
	if flipsStr[c] == 'H':
		h *= -1
	else:
		v *= -1
if h == 1 and v == 1:
	print('1 2')
	print('3 4')
elif h == -1 and v == 1:
	print('3 4')
	print('1 2')
elif h == 1 and v == -1:
	print('2 1')
	print('4 3')
else:
	print('4 3')
	print('2 1')