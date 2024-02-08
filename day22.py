input = open('in22').read().strip().split('\n')

input = [i.split() for i in input[2:]]
#name, size, used, available
input = sorted(input,key=lambda x: int(x[3][:-1]))
res = 0
for i in input:
	used = int(i[2][:-1])
	if used == 0:
		continue
	for j in input:
		a = int(j[-2][:-1])
		if used <= a and j != i:
			res += 1 	

print(res)

input = [i.split() for i in open('in22').read().strip().split('\n')[2:]]
kaart = {}
for i in input:
	_,x,y = i[0].split('-')	
	kaart[(int(x[1:]),int(y[1:]))] = [int(i[2][:-1]),int(i[3][:-1])]

#finding the maximum values:
mx = 0
my = 0
for i in kaart:
	x,y = i
	if x > mx:
		mx = x	
	if y > my:
		my = y

#code to visualize the problem
k = []
for y in range(my+1):
	row = ''
	for x in range(mx+1):
		if kaart[x,y][0] == 0:
			s = (x,y)
		row += '-'+(str(kaart[x,y][0])+'/'+str(kaart[x,y][1]))
	k.append(row)

[print(i) for i in k]	

#manual calculations:
up = s[1]
right = mx-s[0]-1
left = (mx-1)*5+1
print(up+left+right+12) #12 is offset for the blocking values
