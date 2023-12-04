lines = []
count = 0

with open('02.txt') as file:
	for line in file:
		line = line.strip("\n")
		line = line.replace(" ", "")
		lines.append(line)

colors = ["red","green","blue"]
rgb = [12,13,14]
sum_id = 0

sum_min = 0

for line in lines:
	#looping through all the games
	rgb_count = [0,0,0]
	words = line.split(":")
	games = words[1].split(";")

	game_num = words[0].replace("Game", "")
	game_num = int(game_num)

	isPossible = True
	max_cubes = [0,0,0]

	for miniSet in games:
		#looping through all the sets of the games
		items = miniSet.split(",")
		#print(items)

		for item in items:
			r,g,b = 0,0,0
			#print(item)
			if "red" in item:
				r = item.replace("red", "")
			if "green" in item:
				g = item.replace("green", "")
			if "blue" in item:
				b = item.replace("blue", "")
			r = int(r)
			g = int(g)
			b = int(b)
			max_cubes[0] = max(max_cubes[0], r)
			max_cubes[1] = max(max_cubes[1], g)
			max_cubes[2] = max(max_cubes[2], b)
		
		# 	if r > rgb[0] or g > rgb[1] or b > rgb[2]:
		# 		isPossible = False
		# 		break
		# if not isPossible:
		# 	break


	if isPossible:
		sum_id += game_num
	cube = max_cubes[0] * max_cubes[1] * max_cubes[2]
	sum_min += cube

print(sum_id)
print(sum_min)