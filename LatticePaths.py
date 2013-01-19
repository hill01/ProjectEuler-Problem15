table = {}

def path(x, y):
	if x == 0 and y == 0:
		return 1
	elif (x, y) in table:
		return table[(x, y)] 
	else:
		resultx = 0
		resulty = 0
		if x > 0: 
			resultx = path(x - 1, y)
			table[(x - 1, y)] = resultx
		if y > 0: 
			resulty = path(x, y - 1)
			table[(x, y - 1)] = resulty
		return resultx + resulty

print path(20,20)
