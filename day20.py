input = open('in20').read().strip().split('\n')
input = sorted([[int(j) for j in i.split('-')] for i in input])
low = 0
for l,u in input:
	if l > low+1:
		print(low+1)
		break
	if l <= low+1 and u > low:
		low = u
	
#part 2
m = 4294967295
low = 0
res = 0
f = True 
for l,u in input:
	if l > low+1:
		low += 1
		res += l-low
	if l <= low+1 and u > low:
		low = u
	if low == m:	
		f = False

if input[-1][-1] < m and f:
	res += m-input[-1][-1]
print(res)
