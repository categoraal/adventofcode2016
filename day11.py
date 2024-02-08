input = open('in11').read().strip().split('\n')
#generators fry chips on the same level that are NOT connected to their own generator

p1 = [4,2,4,0]
p2= [8,2,4,0]

def solve(x):
	res = 0
	for i,v in enumerate(x):
		if i < 3:
			x[i+1] += v		
			res += (v)*2-3
	print(res)

solve(p1)
solve(p2)
