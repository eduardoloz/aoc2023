lines = []
count = 0

with open('04.txt') as file:
	for line in file:
		line = line.strip("\n")
		line = line.split(":")
		line[1] = line[1].split("|")
		lines.append(line)

print(lines)

count_cards = [1] * len(lines)

for i in range(len(lines)):
	counter = 0
	win = [int(x) for x in lines[i][1][0].split()]
	num = [int(x) for x in lines[i][1][1].split()]
	for item in win:
		if item in num:
			counter += 1
	for j in range(i+1,i+1+counter):
		count_cards[j] += 1 * count_cards[i]
	
tot_cards = 0

for num in count_cards:
	tot_cards += num

print(tot_cards)