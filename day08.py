input = open('in8').read().strip().split('\n')

grid = []
for i in range(6):
	row = []
	for j in range(50):
		row.append('.')
	grid.append(row)


for ins in input:
	ins = ins.split(' ')
	print(ins)
	if ins[0] == 'rect':
		col,row = [int(i) for i in ins[1].split('x')]
		for c in range(col):
			for r in range(row):
				grid[r][c] = '#'
	if ins[0] == 'rotate' and ins[1] == 'row':
		row = int(ins[2].split('=')[-1])
		shift = int(ins[-1])
		grid[row] = grid[row][-shift:]+grid[row][:-shift]	
	if ins[0] == 'rotate' and ins[1] == 'column':
		col = int(ins[2].split('=')[-1])
		shift = int(ins[-1])
		grid = list(map(list,zip(*grid)))
		grid[col] = grid[col][-shift:]+grid[col][:-shift]	
		grid = list(map(list,zip(*grid)))
			




[print(''.join(i)) for i in grid]
print(sum([i.count('#') for i in grid]))
# 65 not the right answer
