lines = []

with open('05.txt') as file:
	for line in file:
		line = line.strip("\n")
		lines.append(line)

seeds = [int(x) for x in lines[0].split(":")[1].split()]
spots = []

for i in range(1,len(lines)):
	if ":" in lines[i]:
		spots.append(i)


print("spots is", spots)

maps = [[] for x in range(7)]
simulation = [[0] * len(seeds) for x in range(8)]
simulation[0] = seeds

for i in range(len(spots)):
	num = spots[i]
	for j in range(num+1,len(lines)):
		if ":" in lines[j]:
			break
		elif len(lines[j]) > 0:
			arr = [int(x) for x in lines[j].split()]
			maps[i].append(arr)

print("simulation is" , simulation)

for i in range(len(maps)):
	hit = [0] * len(simulation[i])
	for k in range(len(simulation[i])):
		num = simulation[i][k]
		for j in range(len(maps[i])):
			dst, src, ran = maps[i][j][0], maps[i][j][1], maps[i][j][2],
			if num >= src and num < src + ran:
				hit[k] = 1
				simulation[i+1][k] = dst + num - src
	for k in range(len(simulation[i])):
		if hit[k] == 0:
			simulation[i+1][k] = simulation[i][k]

lastSimulation = simulation[len(simulation)-1]

print(min(lastSimulation))

#use a list of intervals instead of number by number
