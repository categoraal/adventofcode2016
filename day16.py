input = open('in16').read().strip()

def fill(a):
	b = a[::-1]
	n = ''
	for c in b:
		if c == '1':
			n+='0'
		else:
			n+= '1'

	return a+'0'+n

def checksum(x):
	res = ''
	for i in range(int(len(x)/2)):
		if len(set(list(x[2*i:2*i+2]))) == 1:
			res += '1'
		else:	
			res += '0'	
	return res

for part in [1,2]:
	if part == 1:
		l = 272
	if part == 2:
		l = 35651584
	n = input
	while len(n) < l:
		n = fill(n)

	n = n[:l]
	c = checksum(n)
	while len(c)%2 == 0:
		c = checksum(c)

	print(c)
