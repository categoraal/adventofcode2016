import hashlib
input = open('in17').read().strip()

l = len(input)
start = (0,0) 
end = (3,3)

m = hashlib.md5('hijkl'.encode('utf-8')).hexdigest()[:4]
dirs = ('U','D','L','R')
di = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}

queue = [(start,input)]
sols = []
def path(queue):
	for pos,h in queue:
		x,y = pos
		m = hashlib.md5(h.encode('utf-8')).hexdigest()[:4]	
		if pos == end:
			sols.append(h[l:])
			continue
		for i,j in zip(m,dirs):
			if i in 'bcdef':
				dx,dy = di[j]
				nx = x+dx;ny = y+dy
				if 0 <= nx <= 3 and 0 <= ny <= 3:
					queue.append(((nx,ny),h+j))
			
path(queue)
print(sols[0])
print(len(sorted(sols,key=len)[-1]))
