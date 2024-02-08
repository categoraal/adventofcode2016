instructions = [i.split() for i in open('in25').read().strip().split('\n')]


def computer(regs):
	p = 0
	output = []
	while p < len(instructions):
		ins = instructions[p]
		#input('-')
		#print(p,ins,regs)	
		if ins[1] in regs:
			val = int(regs[ins[1]])
		else:
			val = int(ins[1])
		if len(ins) == 3:
			if ins[2] in regs:
				val2 = int(regs[ins[2]])
			else:
				val2 = int(ins[2])
		if ins[0] == 'cpy':
			regs[ins[2]] = val
			p += 1
		if ins[0] == 'jnz':
			if val !=0:
				p += val2
			else:
				p += 1
		if ins[0] == 'inc' and instructions[p+1][0] == 'dec' and  instructions[p+2][0]== 'jnz' and  instructions[p+3][0]== 'dec' and instructions[p+4][0] == 'jnz':
			regs[ins[1]] += (regs[instructions[p+1][1]]) *(regs[instructions[p+3][1]])
			regs[instructions[p+1][1]]=0;regs[instructions[p+3][1]] = 0
			p += 5
			
		elif ins[0] == 'inc':
			regs[ins[1]] += 1
			p += 1
		if ins[0] == 'dec':
			regs[ins[1]] -= 1
			p += 1	
		if ins[0] == 'out':
			output.append(regs[ins[1]])
			p += 1
			if output[0] != 0:
				return False
			if len(output) > 11:
				for i,v in enumerate(output):
					if (i%2==0 and v != 0) or (i%2 == 1 and v != 1):
						return False
				return True
				
		if ins[0] == 'tgl':
			np = p+val
			if 0<= np < len(instructions):
					if len(instructions[np]) == 2:
						if instructions[np][0] == 'inc':
							instructions[np][0] = 'dec'
						else:
							instructions[np][0] = 'inc'
					if len(instructions[np]) == 3:
						if instructions[np][0] == 'jnz':
							instructions[np][0] = 'cpy'
						else:
							instructions[np][0] = 'jnz'

			p+=1
		
	return regs['a']


check = False
i = 0
while check == False:	
	i += 1
	regs = {'a':i,'b':0,'c':0,'d':0}	
	check = (computer(regs))

print(i)
