from copy import deepcopy
input = open('in10').read().strip().split('\n')

values = [[],[]] 
bots = {}
bots_list = []
output = {}
for i in input:
	i = i.split()
	if i[0] == 'bot':
		bots[i[0]+i[1]] = [i[5]+i[6],i[-2]+i[-1],]
		bots_list.append(int(i[1]))
		if i[-2] == 'output':
			output[i[-2]+i[-1]] = ''
		if i[5] == 'output':
			output[i[5]+i[6]] = ''
	if i[0] == 'value':
		values[0].append(i[1]) 
		values[1].append(i[-2]+i[-1])	

def findd(values):
	doubles = []
	for i in set(values[1]):
		if values[1].count(i) == 2:
			doubles.append(i)
	return doubles
				
def remap(doubles,x):
	newvalues = deepcopy(values)	
	for double in doubles:
		idxs,vals = [],[]
		for idx,val in enumerate(values[1]):
			if val == double:
				idxs.append(idx)
				vals.append(values[0][idx])	
			
			if '61' in vals and '17' in vals and x:
				print(double) 
				x = False

		if int(vals[0]) < int(vals[1]):
			newvalues[1][idxs[0]] = bots[double][0]
			newvalues[1][idxs[1]] = bots[double][1]
		else:
			newvalues[1][idxs[0]] = bots[double][1]
			newvalues[1][idxs[1]] = bots[double][0]
	return newvalues,x

x = True
while True:
	doubles = findd(values)
	oldvalues =	deepcopy(values) 
	values,x = remap(doubles,x)
	if oldvalues == values:
		break

res = 1
for idx,val in enumerate(values[1]):
	if val[-2:] == 't0' or val[-2:] =='t1' or val[-2:] == 't2':
		res = res * int(values[0][idx])	
print(res)
