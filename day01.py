input = open('in1').read().strip().split(', ')

locx = 0
locy = 0
locs = {(0,0)}
dirs = [(-1,0),(0,1),(1,0),(0,-1)] #N,E,S,W
dc = 0 
flag = True 

for instruction in input:
	dist = int(instruction[1:])
	if instruction[0] == 'R':
		dc += 1
	else:
		dc -= 1
	dy = dirs[dc%4][0]*dist
	dx = dirs[dc%4][1]*dist
	locy += dy 
	locx += dx 
	if flag: 
		if dy != 0:
			for i in range(0,dy,int(abs(dy)/dy)):
				if (locy-i,locx) in locs:
					ans2 = (abs(locy-i)+abs(locx))
					flag = False
				locs.add((locy-i,locx))			
		if dx != 0:
			for i in range(0,dx,int(abs(dx)/dx)):
				if (locy,locx-i) in locs:
					asn2 = (abs(locy),abs(locx-i))
					flag = False
				locs.add((locy,locx-i))
print(abs(locx)+abs(locy))
print(ans2)
