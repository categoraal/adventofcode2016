from itertools import permutations
kaart = open('in24').read().strip().split('\n')
[print(k) for k in kaart]

letters = {}
for y in range(len(kaart)):
	for x in range(len(kaart[0])):
		if kaart[y][x] not in '#.':
			letters[kaart[y][x]] = (x,y)	

def route(letter):
	dirs = ((1,0),(-1,0),(0,1),(0,-1))
	queue = [letters[letter]]
	seen = {letters[letter]:0}
	for x,y in queue:
		d = seen[(x,y)]
		for dx,dy in dirs:
			nx = x+dx;ny=y+dy	
			if 0 < nx < len(kaart[0]) and 0 < ny < len(kaart) and (nx,ny) not in seen and kaart[ny][nx] != '#':
				queue.append((nx,ny))
				seen[(nx,ny)] = d+1
	res = {}		
	for i in letters:
		if i != letter:
			res[i] = seen[letters[i]]		
	return res

graph = {}
for i in letters:
	graph[i] = route(i)

res = []
for i in permutations('1234567',7):
	d = 0
	c = '0'
	for l in i:
		d += graph[c][l]	
		c = l
	res.append(d)	
print(min(res))

res = []
for i in permutations('1234567',7):
	d = 0
	c = '0'
	for l in i:
		d += graph[c][l]	
		c = l
	d += graph[c]['0']
	res.append(d)	
print(min(res))
