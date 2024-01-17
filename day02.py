input = open('in2').read().strip().split('\n')

grid = ['123','456','789']
dirs = {'U':(-1,0),'L':(0,-1),'D':(1,0),'R':(0,1)}
pos = [1,1]
key = ''
for string in input:
	pos = [1,1]
	for c in string:
		dy,dx = dirs[c]
		ny = pos[0] + dy		
		nx = pos[1] + dx
		if 0 <= ny <= 2:
			pos[0] = ny
		if 0 <= nx <= 2:
			pos[1] = nx
	key += grid[pos[0]][pos[1]]

print(key)

## Part 2
grid = ['..1..','.234.','56789','.ABC.','..D..']
key = ''
for string in input:
	pos = [2,0]
	for c in string:
		dy,dx = dirs[c]
		ny = pos[0] + dy		
		nx = pos[1] + dx
		if abs(2-nx)+abs(2-ny) <=2:	
			pos[0] = ny
			pos[1] = nx
	key += grid[pos[0]][pos[1]]

print(key)

		
