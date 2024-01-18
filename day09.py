input = open('in9').read().strip()

res = ''
i = 0
lb = False
wflag = False

wl = ''
rep = ''
while i < len(input):
	if input[i] == '(':
		lb = True
		i += 1
	elif lb and input[i].isdigit() and wflag == False:
		wl += input[i]
		i += 1
	elif lb and input[i] == 'x':
		wflag = True
		i += 1
	elif 	lb and input[i].isdigit() and wflag == True:
		rep += input[i]	
		i += 1
	elif input[i] == ')':
		lb = False
		wflag = False
		i += 1
		res += int(rep)*input[i:i+int(wl)]
		i += int(wl)
		wl = ''
		rep = ''
	else:
		res += input[i]

print(len(res))

## Part 2
## Recursion

def f(x):
	lb = False
	wflag = False
	res = 0
	i = 0
	wl = ''
	rep = ''
	while i < len(x):
		if x[i] == '(':
			lb = True
			i += 1
		elif lb and x[i].isdigit() and wflag == False:
			wl += x[i]
			i += 1
		elif lb and x[i] == 'x':
			wflag = True
			i += 1
		elif lb and x[i].isdigit() and wflag == True:
			rep += x[i]	
			i += 1
		elif x[i] == ')':
			lb = False
			wflag = False
			i += 1
			res += int(rep)*f(x[i:i+int(wl)])
			i += int(wl)
			wl = ''
			rep = ''
		else:
			i += 1
			res += 1
	return res

print(f(input))
