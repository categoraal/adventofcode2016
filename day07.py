input = open('in7').read().strip().split('\n')

def abba(x):
	for i in range(len(x)-3):
		if x[i:i+2] == x[i+3:i+1:-1] and x[i] != x[i+1]:
			return True
	return False

cnt = 0
for i in input:
	condition = False
	i = i.replace('[',']')
	i = i.split("]")
	for idx, word in enumerate(i):
		if abba(word) and idx%2 == 0:
			condition = True
		elif abba(word) and idx%2 == 1:
			condition = False
			break
	if condition:
		cnt += 1

print(cnt)
# 110 too high
# Part 2
def aba(x):
	res = []
	for i in range(len(x)-2):
		if x[i] == x[i+2] and x[i] != x[i+1]:
			res.append(x[i:i+2])
	return res
	
p2 = 0
for i in input:
	condition = False
	i = i.replace('[',']')
	i = i.split("]")
	set1 = set()
	set2 = set()
	for idx,word in enumerate(i):
		abas = aba(word)
		if idx%2 == 0:
			for w in abas:
				set1.add(w)	
		if idx%2 == 1:
			for w in abas:
				set2.add(w[::-1])
	if len(set1&set2) > 0:
		p2 += 1

print(p2)
