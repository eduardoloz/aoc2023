
lines = []
count = 0

with open('04.txt') as file:
	for line in file:
		line = line.strip("\n")
		line = line.split(":")
		line[1] = line[1].split("|")
		lines.append(line)

print(lines)

tot_points = 0

for lines in lines:
	multiplier = 0
	win = [int(x) for x in lines[1][0].split()]
	num = [int(x) for x in lines[1][1].split()]
	for item in win:
		if item in num:
			#print(lines[0], item)
			multiplier += 1
	print(line[0], multiplier)
	tot_points += int(pow(2, multiplier-1))

print(tot_points)