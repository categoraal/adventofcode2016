input = open('in15').read().strip().split('\n')

nums = []
for i in input:
	i = i.split()
	nums.append([int(i[3]),int(i[-1][:-1])])	

print(nums)

def pos(t,n,o):
	return (t+o)%n

def f(nums):
	t = 0
	condition = True
	while condition:
		i = 1
		res = []
		for n,o in nums:
			res.append(pos(t+i,n,o))
			i += 1
		if sum(res) == 0:
			return t
			condition = False	
		t += 1

print(f(nums))
nums.append([11,0])
print(f(nums))
#too high 203661
