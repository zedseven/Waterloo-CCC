t = int(input())
cases = []

def isPrime(a):
	return all(a % i for i in range(2, a))

for i in range(t):
	cases.append(int(input()))
for case in cases:
	if isPrime(case):
		print(str(case) + ' ' + str(case))
		continue
	if case % 2 == 0:
		v = 1
	else:
		v = 2
	n = case - v
	x = case + v
	while not (isPrime(n) and isPrime(x)):
		n -= 2
		x += 2
	print(str(n) + ' ' + str(x))