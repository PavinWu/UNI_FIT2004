"""
longest increasing subsequence problem
"""
def long_inc_sub(seq):
	"""
	seq is the sequence to find the longest subsequence
	"""
	max_subsq_array = [1]	# contain the max subsequence length possble for the item in the corresponding entry
	for i in range(1, len(seq)):
		crnt_max_subsq = 0				# max subsequence for the new number at entry i (0 in case item at i is the minimum in list)
		for j in range(i-1, -1, -1):			# search through max_subsq_array
			if seq[i] > seq[j] and max_subsq_array[j] >= crnt_max_subsq:		# if new item is larger (i.e. can form new sequence) and has larger len than current
				crnt_max_subsq = max_subsq_array[j]							# store the largest length found so far
		max_subsq_array.append(crnt_max_subsq + 1)
	
	"""
	# Get the index and the subsequence.
	# too tired to do.
	
	sub_sq = [[len(max_subsq_array)-1, seq[-1]]]
	crnt_long_inc_subsq = max_subsq_array[-1]
	for i in range(len(max_subsq_array), -1, -1):
		if seq[i] < sub_sq and max_subsq_array[i] == crnt_long_inc_subsq - 1:
			sub_sq_index.append([i, seq[i]])
	"""
	return max_subsq_array


if __name__ == "__main__":
	seq = [0, 8, 4, 12, 2, 10, 6, 14, 9, 5, 16, 3, 11, 7, 1]
	print(max(long_inc_sub(seq)))
    