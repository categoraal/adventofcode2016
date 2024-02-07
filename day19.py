from copy import deepcopy
input = int(open('in19').read().strip())

l = [i for i in range(1,1+input)]
i = 0
while len(l) > 1:
	nl = []
	while i < len(l):
		nl.append(l[i])
		i += 2
	if l[-1] != nl[-1]:
		l = deepcopy(nl)
	else:
		l = deepcopy(nl[1:])
	i = 0
print(l[0])

def solve(n):
	l = [i for i in range(1,1+n)]
	i = 0
	while len(l) != 1:
		d = len(l)//2
		c = (i+d)%len(l)
		l.pop(c)
		if c > i:
			i += 1	
		if i >= len(l):
			i = 0
	return l[0]

#for i in range(1,100):
#	print(i,solve(i))

def p2(n):
	i = 1
	while i < n:
		i*=3
		if i == n:
			return i
	d = i-n		
	return int(n-i/3)
print(p2(input))
