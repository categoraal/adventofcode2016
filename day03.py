import re
input = open('in3').read().strip().split('\n')

cnt = 0
allnums = []
for string in input:
	nums = [int(i) for i in re.findall(r'\d+',string)]
	allnums.append(nums)
	nums = sorted(nums)
	if sum(nums[:2]) > nums[-1]:
		cnt += 1		
print(cnt)
# part 2

allnums = list(map(list,zip(*allnums)))
allnums = [i for j in allnums for i in j]
cnt = 0
for i in range(len(allnums)):
	if i%3 == 0:
		nums = sorted(allnums[i:3+i])
		if sum(nums[:2]) > nums[-1]:
			cnt += 1	

print(cnt)

#too low 1512
