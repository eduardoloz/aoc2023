lines = []
count = 0

with open('03.txt') as file:
	for line in file:
		line = line.strip("\n")

		lines.append(line)
	

def inBox(row, col):
	return (row >= 0 and col >= 0 and row < len(lines) and col < len(lines[0]))

big_sum = 0

valid_nums = []

for i in range(len(lines)):
	currentNum = ""
	start, end = 0, 0
	multiplication = False

	for j in range(len(lines[0])):
		
		if lines[i][j].isdigit():
			currentNum += lines[i][j]
			end = j
			if len(currentNum) == 0:
				start = j
			if j == len(lines[0])-1:
					if len(currentNum) > 0:
						valid_nums.append([i, start,end])
		else:
			if len(currentNum) > 0:
				valid_nums.append([i,start,end])
			start = j+1
			currentNum = ""
			
gearboxes = {}

for ran in valid_nums:
	row = ran[0]
	start = ran[1]
	end = ran[2]

	print(lines[row][start:end+1])

	for x in range(row-1, row+2):
		for y in range(start-1, end+2,1):
			if inBox(x, y):
				if lines[x][y]=='*':
					if (x,y) not in gearboxes:
						gearboxes[(x,y)] = []
					gearboxes[(x,y)].append(ran)

product_sum = 0

for box in gearboxes:
	if len(gearboxes[box]) == 2:
		val1 = int(lines[gearboxes[box][0][0]][gearboxes[box][0][1]:gearboxes[box][0][2]+1])
		val2 = int(lines[gearboxes[box][1][0]][gearboxes[box][1][1]:gearboxes[box][1][2]+1])
		product_sum += (val1 * val2)
          
          
print(product_sum)

