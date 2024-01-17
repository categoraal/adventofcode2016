import hashlib
input = open('in5').read().strip()
c = 0
condition = True
key = ''
key2 = [0,1,2,3,4,5,6,7]
cnt = 0
first = set()
while condition:
	m = hashlib.md5((input+str(c)).encode('utf-8')).hexdigest()
	c += 1
	if m.startswith('00000'):
		if len(key) < 8:
			key += m[5]
		if len(key) == 8 and cnt == 8:
			condition = False
		val = m[6]
		if m[5].isdigit() and int(m[5]) < 8:
			if int(m[5]) not in first:
				cnt += 1
				key2[int(m[5])] = str(m[6])		
			first.add(int(m[5]))
print(key)
print(''.join(key2))
