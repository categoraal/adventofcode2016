input = [i.split() for i in open('in12').read().strip().split('\n')]
[print(i) for i in input]

regs = {'a':0,'b':0,'c':0,'d':0}

def computer(regs):
	p = 0
	while p < len(input):
		ins = input[p]
		if ins[1] in regs:
			val = int(regs[ins[1]])
		else:
			val = int(ins[1])

		if ins[0] == 'cpy':
			regs[ins[2]] = val	
			p += 1
		if ins[0] == 'jnz':
			if val !=0:	
				p += int(ins[2])
			else:
				p += 1	
		if ins[0] == 'inc':
			regs[ins[1]] += 1
			p += 1
		if ins[0] == 'dec':
			regs[ins[1]] -= 1
			p += 1
	return regs['a']
	#print(p)
	#print(regs)

print(computer(regs))
print(computer({'a':0,'b':0,'c':1,'d':0}))

