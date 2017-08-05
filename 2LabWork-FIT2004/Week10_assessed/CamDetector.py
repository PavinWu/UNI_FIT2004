######	 Heap operations	######
# operations are mod so: works with tuple, and update dist's (distance's) index in heap on finalList

# info is a list containing path to reach current heap. Update shortest path during Dij's alg  
def minDijHeap_insert(heap, ID, dist, info, finalList):	# upHeap
	if heap == []:
		heap = [None]	# skip index 0

	heap.append((ID, dist, info))
	currentIndex = len(heap)-1
	finalList[ID] = currentIndex	# in case it never gets into the loop
	if ID == 1191:
		print(currentIndex)
	while currentIndex//2 > 0 and heap[currentIndex//2][1] > dist:	# must check NoneType Error first
		finalList[heap[currentIndex][0]], finalList[heap[currentIndex//2][0]] = currentIndex//2, currentIndex  	## Have to update index before swap value! (since index to change index come from ID in value)
		## swap value first (then change index later) will make index in finalList still refer to same node within iteration
		heap[currentIndex//2], heap[currentIndex] = heap[currentIndex], heap[currentIndex//2]
		#finalList[ID], finalList[heap[currentIndex//2][0]] = currentIndex//2, currentIndex  	## check
		currentIndex = currentIndex//2
	return heap, finalList
		
def minDijHeap_delete(heap, finalList):	# downHeap + deleteMin
	root = heap[1]
	heap[1] = heap[-1]
	heap = heap[:-1]	# throw away last (i.e. take all until -1)
	
	moveNodeIndex = 1
	minChildIndex = _findMinChild(heap, moveNodeIndex)
	while minChildIndex < len(heap) and heap[moveNodeIndex][1] > heap[minChildIndex][1]:
		finalList[heap[minChildIndex][0]] = moveNodeIndex	# moved child up (node with ID at minChild now at moveNode (above))
		finalList[heap[moveNodeIndex][0]] = minChildIndex	# moved down
		heap[moveNodeIndex], heap[minChildIndex] = heap[minChildIndex], heap[moveNodeIndex]
		# finalList[heap[minChildIndex][0]] = moveNodeIndex	# moved child up (node with ID at minChild now at moveNode (above))
		# finalList[heap[moveNodeIndex][0]] = minChildIndex	# moved down
		moveNodeIndex = minChildIndex	
		minChildIndex = _findMinChild(heap, moveNodeIndex)	# get new child to check
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
		# print('Too late to help!!!!!!')
		return	
	
	finalList[userLoc] = 1
	camFound = []
	while len(discoveredHeap) > 1 and len(camFound) < k:	# >1 since we also have None
		currentLocNode, discoveredHeap, finalList = minDijHeap_delete(discoveredHeap, finalList)
		# print('eee' + str(currentLocNode))	###
		# print(currentLocNode[0], discoveredHeap, len(discoveredHeap))	###
		if isCam[currentLocNode[0]]:		# go one at a time when going next vertex. if not put Cam node in the way of path -> will not go pass cam
			camFound.append(currentLocNode)			
		elif finalList[currentLocNode[0]] != -1:
			print('***' + str(currentLocNode))
			for u in adjList[currentLocNode[0]]:
				### print(u[0])		###
				print(finalList[1191])
				#print(finalList[u[0]])	###	89, 6: u[0] is None
				#print(discoveredHeap[finalList[u[0]]])	###
				if not u[2] and u[0] is not None:			# not TOLL and not Terminal 
					### print('len: '+ str(len(discoveredHeap)))	###
					#print(discoveredHeap[finalList[u[0]]])
					### if finalList[u[0]] != -2:		###
					###	print('	' + str(finalList[u[0]]))	###
					###	print(discoveredHeap)	###
					if finalList[u[0]] == -2: 	# not in discovered (don't have to search heap!)
						discoveredHeap, finalList = minDijHeap_insert(discoveredHeap, u[0], 
								currentLocNode[1]+u[1], currentLocNode[2]+[u[0]],finalList)
					elif finalList[u[0]] != -1 and discoveredHeap[finalList[u[0]]][1] > currentLocNode[1]+u[1]:
						u_indx = finalList[u[0]]
						prev_u = discoveredHeap[u_indx]
						discoveredHeap[u_indx] = (prev_u[0], currentLocNode[1]+u[1], currentLocNode[2]+[prev_u[2][-1]] )
						while u_indx//2 > 0 and discoveredHeap[u_indx][1] < discoveredHeap[u_indx//2][1]:	# up heap
							finalList[discoveredHeap[u_indx][0]] = u_indx//2
							finalList[discoveredHeap[u_indx//2][0]] = u_indx
							discoveredHeap[u_indx], discoveredHeap[u_indx//2] = discoveredHeap[u_indx//2], discoveredHeap[u_indx]
							u_indx = u_indx//2
					print(discoveredHeap)	###
						
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
	for i in range(totalVertices):
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
	
	# assume valid input
	userLocation = int(input('Enter your location: ').strip())
	k = int(input('Enter k: ').strip())
	
	camFoundList = findCam(userLocation, k, adjList, finalizedList, isCamList)
	if camFoundList is None:
		print('Too late to help!!!!!!')
	else:
		for i in range(len(camFoundList)):
			print()
			print('Camera ' + str(i+1) + ': ' + str(camFoundList[i][0]))
			print('Distance from your location: ' + str(camFoundList[i][1]))
			print('Shortest path: ', end='')
			for vertex in camFoundList[i][2][:-1]:	# not take last
				print(vertex, end=' --> ')
			print(camFoundList[i][2][-1])	# so we can put here without arrow
	# print(camFoundList)
	