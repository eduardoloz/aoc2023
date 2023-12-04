lines = []
count = 0

with open('03.txt') as file:
	for line in file:
		line = line.strip("\n")

		lines.append(line)
	

def inBox(row, col):
	return (row >= 0 and col >= 0 and row < len(lines) and col < len(lines[0]))

big_sum = 0

for i in range(len(lines)):
	currentNum = ""
	start, end = 0, 0
	addition = False
	
	for j in range(len(lines[0])):

		if lines[i][j].isdigit():
			if len(currentNum) == 0:
				start = j
			currentNum += lines[i][j]
			end = j
			print(currentNum)
			if j == len(lines[0])-1:
				print(currentNum, i, start, end)
				for x in range(i-1, i+2,1):
					for y in range(start-1, end+2,1):
						if inBox(x, y):
							if lines[x][y] != "." and (not lines[x][y].isdigit()):
								addition = True
								break
					if addition:
						break

				if addition:
					#print("valid num", currentNum)
					big_sum += int(currentNum)
					currentNum = ""
					start, end = j,j
					addition = False
				currentNum = ""
				start, end = j,j
				addition = False
		
		elif currentNum != "" or (j == len(lines[0])-1 and lines[i][j].isdigit()):
			print(currentNum, i, start, end)
			for x in range(i-1, i+2,1):
				for y in range(start-1, end+2,1):
					if inBox(x, y):
						if lines[x][y] != "." and (not lines[x][y].isdigit()):
							addition = True
							break
				if addition:
					break

			if addition:
				#print("valid num", currentNum)
				big_sum += int(currentNum)
				currentNum = ""
				start, end = j,j
				addition = False
			currentNum = ""
			start, end = j,j
			addition = False

	
print(big_sum)

