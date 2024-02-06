ins = open('in21').read().strip().split('\n')


key = 'abcdefgh'

def f(key):
	for i in ins:
		i = i.split()
		if i[0] == 'swap' and i[1] == 'position':
			c1 = key[int(i[2])]; c2 = key[int(i[-1])]
			key = list(key)
			key[int(i[2])] = c2;key[int(i[-1])] = c1
			key = ''.join(key)
		if i[0] == 'swap' and i[1] == 'letter':
			c1 = key.find(i[2]); c2 = key.find(i[-1])
			key = list(key)
			key[c1] = i[-1];key[c2] = i[2]
			key = ''.join(key)
		if i[0] == 'rotate' and i[1] == 'left':
			s = int(i[-2])%len(key)
			key = key[s:]+key[:s]
		if i[0] == 'rotate' and i[1] == 'right':
			s = int(i[-2])%len(key)
			key = key[-s:]+key[:-s]
		if i[0] == 'rotate' and i[1] == 'based':
			s = key.find(i[-1])
			s = s+1 if s < 4 else s+2
			s = s%len(key)
			key = key[-s:]+key[:-s]
		if i[0] == 'reverse':
			a = int(i[2]); b = int(i[-1])
			key = key[:a]+key[a:b+1][::-1]+key[b+1:]
		if i[0] == 'move':
			x = int(i[2]);y = int(i[-1])
			key = list(key)
			c = key.pop(x)
			key = ''.join(key)
			key = key[:y]+c+key[y:]
	return key

print(f(key))

from itertools import permutations
key = 'fbgdceah'

for i in permutations(key,len(key)):
	if f(''.join(i)) == key:
		print(''.join(i))
		break
