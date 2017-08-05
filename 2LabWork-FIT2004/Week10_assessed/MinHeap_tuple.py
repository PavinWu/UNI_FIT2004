"""
NOTE: This is modified version of MinHeap.
It stores a tuple in each node and use the 0th entry to construct heap

HEAP:
root node is at index n. leftChild is at index 2n. rightChild is at index 2n + 1.
Looking at child: root node is at index n//2. Since start at index 1, len of list is the last index
"""

def minHeap_insert(heap, key, info):	# upHeap
	"""
	inputs: heap array, key to insert
	output: heap with inserted key

	Look at root: if less, go up. Otherwise, stay.
	(matter to take less sibling?): if less than parent, then sure less than the sibling.
		: if more than parent, doesn't matter if less or more than sibling: still valid structure
	"""	
	if heap == []:
		heap = [None]	# skip index 0

	heap.append((key, info))
	currentIndex = len(heap)-1
	while currentIndex//2 > 0 and heap[currentIndex//2][0] > key:	# must check NoneType Error first
		heap[currentIndex//2], heap[currentIndex] = heap[currentIndex], heap[currentIndex//2]
		currentIndex = currentIndex//2
	return heap
		
def minHeap_delete(heap):	# downHeap + deleteMin
	"""
	delete root (item at index 1 of heap) and return it
	Also return heap
	"""
	root = heap[1]
	heap[1] = heap[-1]
	heap = heap[:-1]	# throw away last (i.e. take all until -1)
	
	heap = _downHeap(heap, 1)
	return root, heap

def minHeapify(array):
	"""
	To create: call minHeap_insert multiple times
	To make existing array a heap: use this.
	
	@pre-condition: first index of array must be None or an element of the array
	"""
	if array[0] is not None:
		array = [None] + array
		
	N = len(array) - 1
	for i in range(N, 0, -1):	# ends at 1
		array = _downHeap(array, i)
	return array
	
def _downHeap(heap, parentIndex):
	minChildIndex = _findMinChild(heap, parentIndex)
	while minChildIndex < len(heap) and heap[parentIndex][0] > heap[minChildIndex][0]:
		heap[parentIndex], heap[minChildIndex] = heap[minChildIndex], heap[parentIndex]
		parentIndex = minChildIndex
		minChildIndex = _findMinChild(heap, parentIndex)
	return heap
	
def _findMinChild(heap, parentIndex):
	# if statement below works for both when only one child (i.e. left) or no child (kicked out of above loop if no child: know that 2*parentIndex node not exist)
	if 2*parentIndex + 1 >= len(heap) or heap[2*parentIndex][0] < heap[2*parentIndex + 1][0]:
		return 2*parentIndex
	else:
		return 2*parentIndex + 1

"""
if __name__ == "__main__":
	# heap = [None, 3, 9, 11, 15, 18, 13, 14, 17, 19, 23, 20]
	array = [(11,'a'), (19,'b'), (13,'c'), (9,'d'), (23,'e'), (4,'f'), (14,'g')
				, (17,'h'), (15,'i'), (18,'j'), (29,'k')]
	# array = [10,9,8,7,6,5,4,3,-1]
	heap = minHeapify(array)
	print(heap)
	heap = minHeap_insert(heap, 1, 'l')
	print(heap)
	min, heap = minHeap_delete(heap)
	print(min, heap)
"""