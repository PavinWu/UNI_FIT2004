class AVLNode:
	def __init__():
		#self.value = 0;		# can't use 0: 'Any Distinct Integer'
		self.value = None
		self.lChild = None
		self.rChild = None
		self.balanceFactor = 0
		
		self.parent = None
		
class AVLtree:
	def __init__(self):
		self.root = AVLNode()
	
	def search(self, key):	# exactly as BST
		current = self.root
		while True:
			if current is None:		# empty node
				return False
			else:					# if node not None, node has value (value not None too)
				if current.value < key:	
					current = current.rChild
				elif current.value == key:
					return True
				else:
					current = current.lChild

	def insert(self, key):		# insert when found child is None 
		if self.root.value is None:
			self.root.value = key
		else:
			current = self.root
			keyNodeReady = False
			while not keyNodeReady:
				if key < current.value:
					if current.lChild is None:
						current.balanceFactor += 1
						keyNodeReady = True
						# current = current.lChild	# can we link then make node with the link? (instead of directly) 
						current.lChild = AVLNode()
						current.lChild.parent = current
					current = current.lChild
				elif key > current.value:
					if current.rChild is None:
						current.balanceFactor -= 1
						keyNodeReady = True
						current.rChild = AVLNode()
						current.rChild.parent = current	# BUT BF not affect just parent node!
							# can't adjust every step since BF might not change (i.e. when fill in sibling)
							# immediate parent's BF always change, but not always BF of grandPa
					current = current.rChild
				else:
					print("Key Already existed")
					keyNodeReady = True		
			# current = AVLNode()
			current.value = key
			
			keepAVL(current)
			
	def delete(self, key):
		
	
	def keepAVL(self, current):
		"""
		maintain AVL tree structure starting from node with latest change (i.e. current)
		"""
		if current.root.balanceFactor > 1 or current.root.balanceFactor < -1:
			

if __name__ == "__main__":
	keys = [19, 23, 13, 7, 73, 3, 18, 17, 11]
	tree = AVLtree()
	for key in keys:
		tree.insert(key)
		

	