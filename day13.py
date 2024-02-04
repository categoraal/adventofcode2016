input = int(open('in13').read())

def f(x,y,n): 
	return  bin(x*x + 3*x + 2*x*y + y + y*y+n)[2:].count('1')%2

end = (31,39)
start = (1,1)
dist  = {start:0}
queue = [start]
dirs = ((0,1),(0,-1),(1,0),(-1,0))
n = input
for x,y in queue:
	d = dist[(x,y)]
	if (x,y) == end:
		print(d)
	for dx,dy in dirs:
		nx = x+dx;ny = y+dy
		if nx >= 0 and ny >= 0 and (nx,ny) not in dist and f(nx,ny,n) == 0:
			dist[(nx,ny)] = d+1 
			queue.append((nx,ny))

cnt = 0
for i in dist:
	if dist[i] <= 50:
		cnt += 1

print(cnt)
