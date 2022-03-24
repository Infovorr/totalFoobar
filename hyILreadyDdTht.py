def hyILreadyDdTht(n, b):
	k = len(n)
	x = [i for i in str(n)]
	pastValues = [str(n)]
	while (1):
		x.sort(reverse = True)
		y = x[:]
		y.sort()
		xNum = int(''.join(x), b)
		yNum = int(''.join(y), b)
		zNum = xNum - yNum
		if (b != 10):
			newZNum = ''
			while zNum:
				newZNum = str(zNum % b) + newZNum
				zNum //= b
			zNum = newZNum
		x = [i for i in str(zNum)]
		if (len(x) < k):
			x = (['0'] * (k - len(x))) + x
		xTemp = ''.join(x)
		if (xTemp in pastValues):
			distance = len(pastValues) - pastValues.index(xTemp)
			return distance
		pastValues.append(xTemp)
