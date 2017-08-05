######	 Heap operations	######
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
		minChildIndex = _findMinChild(heap, moveNodeIndex)	# get new child to check
	# finalList[heap[moveNodeIndex][0]] = minChildIndex	# moved down
	return root, heap, finalList
	
def _findMinChild(heap, parentIndex):
	# if statement below works for both when only one child (i.e. left) or no child (kicked out of above loop if no child: know that 2*parentIndex node not exist)
	if 2*parentIndex + 1 >= len(heap) or heap[2*parentIndex][1] < heap[2*parentIndex + 1][1]:
		return 2*parentIndex
	else:
		return 2*parentIndex + 1
		
		
######	 Main operations	######
def findCam(userLoc, k, adjList, finalList, isCam):
	"""
	Use a modified Dijkstra's algorithm to shortest path problem.
	Store 'discovered vertices' with MinHeap_tuple 
	"""
	discoveredHeap = [None, (userLoc, 0, [userLoc])]	# (distance, location)
	
	if isCam[userLoc]:
		print('Too late to help!!!!!!')
		return	
	
	finalList[userLoc] = 1
	camFound = []
	while len(discoveredHeap) > 1 and len(camFound) < k:	# >1 since we also have None
		currentLocNode, discoveredHeap, finalList = minDijHeap_delete(discoveredHeap, finalList)
		print(currentLocNode[0], discoveredHeap, len(discoveredHeap))	###
		if isCam[currentLocNode[0]]:		# go one at a time when going next vertex. if not put Cam node in the way of path -> will not go pass cam
			camFound.append(currentLocNode)			
		else:
			for u in adjList[currentLocNode[0]]:
				if not u[2] and u[0] is not None:			# not TOLL and not Terminal 
					if finalList[u[0]] == -2: 	# not in discovered (don't have to search heap!)
						minDijHeap_insert(discoveredHeap, u[0], currentLocNode[1]+u[1], 
											currentLocNode[2]+[u[0]],finalList)
					elif finalList[u[0]] != -1 and discoveredHeap[finalList[u[0]]][1] > currentLocNode[1]+u[1]:
						u_indx = finalList[u[0]]
						prev_u = discoveredHeap[u_indx]
						discoveredHeap[u_indx] = (prev_u[0], currentLocNode[1]+u[1], currentLocNode[2]+[prev_u[2][-1]] )
		
		finalList[currentLocNode[0]] = -1		# Move currentLocNode from discovered to Finalized 
	
	return camFound
		
if __name__ == "__main__":
	"""
	Assume starting edges are ordered
	"""
	totalVertices = 6105
	#adjList = [[]]	# for nodeX -> [... [nodeX_linked1, nodeX_linked2, ...] ...]
	# adjList = [[]]*totalVertices	# if do this, appending to a block also does it to every other block
	adjList = []
	for i in range(6105):
		adjList.append([])
	
	f_edge = open('edges.txt', 'r')
	currentIndex = 0
	for line in f_edge:
		s_inLine = line.split()
		currentLoc = int(s_inLine[0])
		nextLoc = int(s_inLine[1])
		distance = float(s_inLine[2])
		if len(s_inLine) < 4:
			TOLL = False
		else:
			TOLL = True
		
		#if currentLoc == currentIndex:	# same edge
		#	adjList[currentLoc].append((nextLoc, distance, TOLL))	## This graph should be bidirectional ##FIX!!!: know: next v in file always forward
		if currentLoc > currentIndex:		# (strictly) empty edges (no next)
			for i in range(currentIndex, currentLoc):
				adjList[currentIndex].append((None, 0, False))	# no more connected node
				currentIndex += 1
				
		adjList[currentLoc].append((nextLoc, distance, TOLL))
		
		# print(currentLoc, nextLoc, currentIndex)
		
		adjList[nextLoc].append((currentLoc, distance, TOLL))
		if currentLoc >= currentIndex:	# just == is acually ok
			currentIndex += 1
			
	finalizedList = [-2]*totalVertices
	isCamList = []
	f_cam = open('vertices.txt', 'r')
	for line in f_cam:
		s_inLine = line.split()
		currentLoc = int(s_inLine[0])
		for i in range(len(isCamList), currentLoc):
			isCamList.append(False)		# not discovered
		isCamList.append(True)		# cam => not auto finalised: find shortest path first!
		#finalizedList.append(-1)		# cam => auto finalised (can't go pass)
	for i in range(len(isCamList), totalVertices):
		isCamList.append(False)
		
	print(isCamList, len(isCamList))	###
	
	
	# assume valid input
	userLocation = int(input('Enter your location: ').strip())
	k = int(input('Enter k: ').strip())
	
	camFoundList = findCam(userLocation, k, adjList, finalizedList, isCamList)
	print(camFoundList)
	