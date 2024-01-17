input = [list(i) for i in open('in6').read().strip().split('\n')]
input = list(map(list,zip(*input)))

key1 = ''
key2 = ''

for i in input:
	key1 += sorted(i,key=i.count)[-1]
	key2 += sorted(i,key=i.count)[0]

print(key1)
print(key2)


