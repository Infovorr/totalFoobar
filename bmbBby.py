def bmbBby(x, y):
	n, d = max(int(x), int(y)), min(int(x), int(y))
	g = 0
	while d > 1:
		g += n // d
		n, d = d, n % d
	if d == 0:
		return 'impossible'
	g += (n // d) - 1
	return str(g)
