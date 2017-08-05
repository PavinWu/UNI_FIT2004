#####################	 Heap operations	#####################
### operations are mod so: works with tuple, and update dist's (distance's) index in heap on finalList

# info is a list containing path to reach current heap. Update shortest path during Dij's alg  
def minDijHeap_insert(heap, ID, dist, info, finalList):	# upHeap
	if heap == []:
		heap = [None]	# skip index 0

	heap.append((ID, dist, info))
	currentIndex = len(heap)-1
	while currentIndex//2 > 0 and heap[currentIndex//2][1] > dist:	# must check NoneType Error first
		heap[currentIndex//2], heap[currentIndex] = heap[currentIndex], heap[currentIndex//2]
		finalList[ID], finalList[heap[currentIndex//2][0]] = currentIndex//2, currentIndex  	## check
		currentIndex = currentIndex//2
	return heap, finalList
		
def minDijHeap_delete(heap, finalList):	# downHeap + deleteMin
	root = heap[1]
	heap[1] = heap[-1]
	heap = heap[:-1]	# throw away last (i.e. take all until -1)
	
	moveNodeIndex = 1
	minChildIndex = _findMinChild(heap, moveNodeIndex)
	while minChildIndex < len(heap) and heap[moveNodeIndex][1] > heap[minChildIndex][1]:
		heap[moveNodeIndex], heap[minChildIndex] = heap[minChildIndex], heap[moveNodeIndex]
		finalList[heap[minChildIndex][0]] = moveNodeIndex	# moved child up (node with ID at minChild now at moveNode (above))
		moveNodeIndex = minChildIndex	
		minChildIndex = _findMinChild(heap, parentIndex)	# get new child to check
	# finalList[heap[moveNodeIndex][0]] = minChildIndex	# moved down
	finalList[heap[moveNodeIndex][0]] = -1 		# finalised 
	return root, heap, finalList
	
def _findMinChild(heap, parentIndex):
	# if statement below works for both when only one child (i.e. left) or no child (kicked out of above loop if no child: know that 2*parentIndex node not exist)
	if 2*parentIndex + 1 >= len(heap) or heap[2*parentIndex][1] < heap[2*parentIndex + 1][1]:
		return 2*parentIndex
	else:
		return 2*parentIndex + 1
		
		
#####################	 Main operations	#####################
def findCam(userLoc, k, adjList, finalList, isCam):
	"""
	Use a modified Dijkstra's algorithm to shortest path problem.
	Store 'discovered vertices' with MinHeap_tuple 
	"""
	discoveredHeap = [None, (userLoc, 0, [userLoc]))]	# (weight, location)
	
	if finalList[userLoc] == -1:
		print('Too late to help!!!!!!')
		return	
	
	finalList[userLoc] = 1
	camFound = []
	while len(discoveredHeap) > 1 and len(camFound) < k:	# >1 since we also have None
		currentLocNode, discoveredHeap, finalList = minDijHeap_delete(discoveredHeap, finalList)
		for nextLocTuple in adjList[currentLoc[0]]:
			if isCam[nextLocTuple[0]]:
				if finalList[nextLocTuple[0]] == -2:	# hit camera
					#camFound.append((nextLocTuple[0], ))	# append right away or wait till find more edfficient path ...
					# cam can't be put to -1 right away. Need to find shortest path to it first
					# just do similar thing with heap
					camFound.append((nextLocTuple[0], currentLocNode[1]+nextLocTuple[1], 
										currentLocNode[2]+[nextLocTuple[0]))
					discoveredCam.append(
			else:
				if finalList[nextLocTuple[0]] == -2:	# not in discovered (don't have to search heap!)
					minDijHeap_insert(discoveredHeap, nextLocTuple[0], currentLocNode[1]+nextLocTuple[1], 
										currentLocNode[2]+[nextLocTuple[0]],finalList)
				
	# don't forget toll
			
	# remember to update finalList when delete node too
		
if __name__ == "__main__":
	"""
	Assume starting edges are ordered
	"""
	totalVertices = 6105
	adjList = [[]]	# for nodeX -> [... [nodeX_linked1, nodeX_linked2, ...] ...]
	f_edge = open('edges.txt', 'r')
	for line in f_edge:
		s_inLine = line.split()
		currentLoc = int(s_inLine[0])
		nextLoc = int(s_inLine[1])
		weight = float(s_inLine[2])
		if len(s_inLine) < 4:
			TOLL = False
		else:
			TOLL = True
		if currentLoc == len(adjList)-1:	# same edge
			adjList[currentLoc].append((nextLoc, weight, TOLL))	
		else: 	# (strictly) next edge, and empty edges (no next)
			if currentLoc > len(adjList):
				for i in range(len(adjList), currentLoc):
					adjList.append([(-1, 0, False)])	# no more connected node
			adjList.append([(nextLoc, weight, TOLL)])
			
	finalizedList = [-2]*totalVertices
	isCamList = []
	f_cam = open('vertices.txt', 'r')
	for line in f_cam:
		s_inLine = line.split()
		currentLoc = int(s_inLine[0])
		for i in range(len(finalizedList), currentLoc):
			isCamList.append(False)		# not discovered
		isCamList.append(True)		# cam => not auto finalised: find shortest path first!
		#finalizedList.append(-1)		# cam => auto finalised (can't go pass)
	
	# assume valid input
	userLocation = int(input('Enter your location: '))
	k = int(input('Enter k: '))
	
	findCam(userLocation, k, adjList, finalizedList, isCamList)
	
	