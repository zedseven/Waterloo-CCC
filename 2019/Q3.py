import copy

def intIfInt(a):
	try:
		return int(a)
	except ValueError:
		return a

rows = []
rows.append(list(map(intIfInt, input().split(' '))))
rows.append(list(map(intIfInt, input().split(' '))))
rows.append(list(map(intIfInt, input().split(' '))))

#Solve the given info
def fillRows(urows):
	yrows = copy.deepcopy(urows)
	for row in yrows:
		if row[0] == 'X' and row[1] != 'X' and row[2] != 'X':
			row[0] = row[1] - (row[2] - row[1])
		elif row[0] != 'X' and row[1] == 'X' and row[2] != 'X':
			row[1] = row[2] - ((row[2] - row[0]) / 2)
		elif row[0] != 'X' and row[1] == 'X' and row[2] != 'X':
			row[2] = row[1] + (row[1] - row[0])
	return yrows
def fillCols(urows):
	yrows = copy.deepcopy(urows)
	for c in range(3):
		if yrows[0][c] == 'X' and yrows[1][c] != 'X' and yrows[2][c] != 'X':
			yrows[0][c] = yrows[1][c] - (yrows[2][c] - yrows[1][c])
		elif yrows[0][c] != 'X' and yrows[1][c] == 'X' and yrows[2][c] != 'X':
			yrows[1][c] = yrows[2][c] - ((yrows[2][c] - yrows[0][c]) / 2)
		elif yrows[0][c] != 'X' and yrows[1][c] == 'X' and yrows[2][c] != 'X':
			yrows[2][c] = yrows[1][c] + (yrows[1][c] - yrows[0][c])
	return yrows

orows = copy.deepcopy(rows)
orows = fillCols(orows)
orows = fillRows(orows)
hrows = copy.deepcopy(orows)

def tryGetValue(x, y, step):
	global hrows
	if hrows[y][0] != 'X' and hrows[y][1] == 'X' and hrows[y][2] == 'X': #step can be anything
		hrows[y][1] = hrows[y][0] + step
		hrows[y][2] = hrows[y][0] + 2 * step
	elif hrows[y][0] == 'X' and hrows[y][1] != 'X' and hrows[y][2] == 'X':
		hrows[y][0] = hrows[y][1] - step
		hrows[y][2] = hrows[y][1] + step
	elif hrows[y][0] == 'X' and hrows[y][1] == 'X' and hrows[y][2] != 'X':
		hrows[y][0] = hrows[y][2] - 2 * step
		hrows[y][1] = hrows[y][2] - step
	for i in range(5):
		hrows = fillCols(hrows)
		hrows = fillRows(hrows)

def checkSquare():
	global hrows
	#print('------')
	#for row in hrows:
	#	print(str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]))#
	for row in hrows:
		if 'X' in row:
			return False
	for row in hrows:
		if (row[2] - row[0]) / 2 + row[0] != row[1]:
			return False
		if int(row[1]) != row[1]:
			return False
	for c in range(3):
		if (hrows[2][c] - hrows[0][c]) / 2 + hrows[0][c] != hrows[1][c]:
			return False
		if int(hrows[1][c]) != hrows[1][c]:
			return False
	return True

def outSquare():
	global hrows
	for row in hrows:
		print(str(int(row[0])) + ' ' + str(int(row[1])) + ' ' + str(int(row[2])))
	exit()

if checkSquare():
	outSquare()
stepBase = 0
step = 0
while True:
	if hrows[2][2] == 'X':
		tryGetValue(2, 2, step)
	elif hrows[0][2] == 'X':
		tryGetValue(0, 2, step)
	elif hrows[2][0] == 'X':
		tryGetValue(2, 0, step)
	elif hrows[0][0] == 'X':
		tryGetValue(0, 0, step)#
	if checkSquare():
		outSquare()
	#print('------')
	#for row in hrows:
	#	print(str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]))
	#print('----')
	#for row in orows:
	#	print(str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]))
	#print('---')
	#for row in rows:
	#	print(str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]))
	#print(step)
	hrows = copy.deepcopy(orows)
	if step == stepBase and step != 0:
		step = -stepBase
	else:
		stepBase += 1
		step = stepBase