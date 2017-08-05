def multiply_matrices(a,b):
    """
    Multiply two matrices A and B (A X B). OF ANY SIZES
    e.g. for 2 x 2
    A = a[1] a[2]	   B = b[1] b[2]
        a[3] a[4]          b[3] b[4]
	
	A x B = 1,1+2,3 1,2+2,4
			3,1+4,3 3,2+4,4
	
	@pre-condition: the matrices are rectangular
    """
    if len(a[1]) != len(b):
		# no. of column of A != no. of row of B
		return -1
        
    ma = len(a)      # no. of row
    na = len(a[1])  # no. of col
    mb = len(b)
    nb = len(b[1])
	
	#c = [[]]	# result matrix
    c = []	
	
    for i in range(ma):		
		# result matrix is of the size ma x nb
		c.append([])
		for j in range(nb):
			dot_prod = 0
			for k in range(na):		# na == mb
				dot_prod += a[i][k]*b[k][j]
			c[i].append(dot_prod)
    return c
			
	
	
if __name__ == "__main__":
	A = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]	# 3 x 3
	B = [[1,2],[3,4],[5,6]]			# 3 x 2
	print(multiply_matrices(A,B))
