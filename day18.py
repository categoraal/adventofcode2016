input = open('in18').read().strip()

def nr(row):
	row = '.'+row+'.'
	res = ''
	for i in range(len(row)-2):
		w = row[i:i+3]
		if w in ['^^.','.^^','^..','..^']:
			res += '^'
		else:
			res += '.'	
	return res

def board(l):
	rows = [input]
	p2 = rows[-1].count('.')
	while len(rows) < l:
		rows.append(nr(rows[-1]))
		p2 += rows[-1].count('.')
	print(p2)

board(40)
board(400000)
