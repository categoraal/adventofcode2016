input = open('in4').read().strip().split('\n')
decoyremoved = []
	
ans1 = 0 
for i in input:
	name,checksum = i.split('[');checksum= checksum[:-1]
	name,ID = [''.join(name.split('-')[:-1]),name.split('-')[-1]]
	
	a = sorted(sorted(name), key = name.count,reverse = True)
	a = ''.join(list(dict.fromkeys(a)))
	if a.startswith(checksum):
		ans1 += int(ID)
		decoyremoved.append(i)
		
print(ans1)

for i in decoyremoved:
	name,checksum = i.split('[');checksum= checksum[:-1]
	name,ID = [' '.join(name.split('-')[:-1]),int(name.split('-')[-1])]
	word = ''	
	for c in name:
		if c == ' ':
			nc = ' '
		else:
			nc = chr(((ord(c)-97+ID)%26)+97)
		word+=nc
	if word == 'northpole object storage':
		print(ID)
