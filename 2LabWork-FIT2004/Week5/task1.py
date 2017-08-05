def basic_edit_dist(s1, s2):
	"""
	s2 is starting string (on top of matrix), s1 is string to reach
	// cost is the minimum cost of converting the input s1 to s2
	s1 is horizontal.
	"""
	cost = []
	cost.append([])
	for i in range(len(s1)+1):
		cost[0].append(i)
	
	for i in range(1, len(s2)+1):
		cost.append([i])
		for j in range(1, len(s1)+1):
			min_dist = min(cost[i][j-1], cost[i-1][j], cost[i-1][j-1])
			if s1[j-1] != s2[i-1]:
				cost[i].append(min_dist + 1)
			else:
				cost[i].append(min_dist)
	for i in cost:
		print(i)
	return cost
	
def find_alignment(s1, s2, cost):
	"""
	Find the alignment of s1, s2 based on the cost matrix. (sum of all the costs)
	The cost matrix can be found from basic_edit_dist() function above.
	
	j goes through horizontally
	"""
	# current index of the backtrack
	j_bkt = len(cost[0]) - 1
	i_bkt = len(cost) - 1		
	alignment = 0
	
	while i_bkt > 0 or j_bkt > 0:
		alignment += cost[i_bkt][j_bkt]
		if j_bkt == 0:		# i > 0. Go up only
			back_min_dist = cost[i_bkt-1][j_bkt]
			i_bkt = i_bkt-1
		elif i_bkt == 0:	# j > 0. Go left only
			back_min_dist = cost[i_bkt][j_bkt-1]
			j_bkt = j_bkt-1
		else:
			back_min_dist = min(cost[i_bkt][j_bkt-1], cost[i_bkt-1][j_bkt], cost[i_bkt-1][j_bkt-1])
			if back_min_dist == cost[i_bkt-1][j_bkt-1]:	# go diagonal
				i_bkt, j_bkt = i_bkt-1, j_bkt-1
				# check diagonal first. If there is same cost at other entry, it will take 
				# equal or more in total cost than going directly diagonal
			elif back_min_dist == cost[i_bkt-1][j_bkt]:		# go up
				i_bkt, j_bkt = i_bkt-1, j_bkt
			
			elif back_min_dist == cost[i_bkt][j_bkt-1]:		# go left
				i_bkt, j_bkt = i_bkt, j_bkt-1
			
	return alignment
	
"""
def find_min(a, b, c):
	#find minimum between three numbers
	
	if b - a >= 0:
		if a - c >= 0:
			return c
		elif a - c < 0: # can't use else ! (since b-a might be in the middle. else will catch it)
			return a
	elif a - b < 0:
		if b - c >= 0:
			return c
		elif b - c < 0:
			return b
	elif c - b >= 0
		if b - a >= 0:
			return a
		else
		
"""
	
	
if __name__ == "__main__":
	s1 = 'Dangder'
	s2 = 'sings'
	cost = basic_edit_dist(s1, s2)
	algmnt = find_alignment(s1, s2, cost)
	print(algmnt)
	
			
		
	
	