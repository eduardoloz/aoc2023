lines = []
count = 0

with open('01.txt') as file:
	for line in file:
		lines.append(line)
		
valid = ['0','1','2','3','4','5','6','7','8','9',
		  'one','two','three','four','five','six','seven','eight','nine']

def number(n):
	if n in valid:
		return True
	return False
sums = 0

def converter(char):
	if char == 'one':
		return '1'
	elif char == 'two':
		return '2'
	elif char == 'three':
		return '3'
	elif char == 'four':
		return '4'
	elif char == 'five':
		return '5'
	elif char == 'six':
		return '6'
	elif char == 'seven':
		return '7'
	elif char == 'eight':
		return '8'
	elif char == 'nine':
		return '9'
	else:
		return char
	
def findFirst(find):
	string = valid[0]
	index = len(find)
	for check in valid:
		num = find.find(check)
		if num < index and num != -1:
			string = check
			index = num
	return converter(string)
	
def findLast(find):
	string = valid[0]
	index = 0
	for check in valid:
		num = find.rfind(check)
		if num > index:
			string = check
			index = num
	return converter(string)

big_sum = 0

for line in lines:
	last = findLast(line)
	if last == '0':
		last = findFirst(line)
	big_num = findFirst(line) + last
	print(findFirst(line), last, big_num)
	big_sum += int(big_num)

print(big_sum)
