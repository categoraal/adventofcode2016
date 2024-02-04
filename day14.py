import hashlib
salt = open('in14').read().strip()

for part in [1,2]:
	potential = []
	keys = set()
	f = True
	end = -1
	i = 0
	while f:
		m = hashlib.md5((salt+str(i)).encode('utf-8')).hexdigest()
		if part == 2:
			for _ in range(2016):
				m = hashlib.md5(m.encode('utf-8')).hexdigest()
		m+='#'
		for idx in range(len(m)-3):
			if m[idx] == m[idx+1] == m[idx+2] != m[idx+3]:
				#print('key',i)
				potential.append((m[idx],i))
				break
		for idx in range(len(m)-5):
			if len(set(m[idx:idx+5])) == 1:
				c = m[idx]
				for p in potential:
					if c == p[0] and 1 <= i - p[1] <= 1000:
						keys.add(p[1])
						if len(keys) == 64:
							#print(potential)
							#print(keys)					
							end = i + 1000;
		if i == end:
			f = False
		i += 1
	#print(m)


	print(sorted(list(keys))[63])

