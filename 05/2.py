import sys

inp = open("05.txt").read().split("\n\n") # splits into seeds / all the maps

seeds = [int(x) for x in inp[0].split()[1:]] #takes in the seeds

changes = [] # ?

for i in range(1, len(inp)): 
	changes.append([[int(x) for x in s.split()] for s in inp[i].split("\n")[1:]])
#returns 2D array with first index the change and 2nd being the mapping in the range


ranges = [[seeds[2*i], seeds[2*i]+seeds[2*i+1]-1] for i in (range(len(seeds)//2))]

print(changes)


#format is [dest, start, increment]
#if something is not in the range, it is mapped to itself

for i in range(len(changes)):
	checked = []

	for j in range(len(changes[i])):
		unchecked = []
		# traverses all the ranges (even the ones we add)
		
		for k in range(len(ranges)):
			dest, start, incr = changes[i][j][0], changes[i][j][1], changes[i][j][2]

			#these are our "line intervals"
			s1, e1, s2, e2 = ranges[k][0], ranges[k][1], start, start + incr - 1

			if  max(s1,s2) <= min(e1,e2):
				# only i2 will be changed as it falls in the mapping interval
				i1 = [min(s1,s2),max(s1,s2)-1] 
				c2 = [max(s1,s2),min(e1,e2)]
				i3 = [min(e1,e2)+1, max(e1,e2)]
				#adding "distances to shift from destination"
				i2 = [c2[0]-start+dest,c2[1]-start+dest]
				checked.append(i2)

				#only care about "extra segments"
				if s1 < s2:
					unchecked.append(i1)
				if e1 > e2:
					unchecked.append(i3)
			
			#add unchecked interval (i.e. we don't have a shared interval)
			else:
				unchecked.append(ranges[k]) 
		
		#need to check with all the mappings from the "transformation block"
		ranges = unchecked
	
	# all our new ranges from mappings we checked - (we're moving onto a new mapping)
	ranges += checked

print(min([r[0] for r in ranges]))







