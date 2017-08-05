def gcd_Euclid(a,b):
    if b>a:		#set a to always be larger
        a, b = b, a
    #print(a,b)

    if b == 0:
        return a
    #elif a == 0:
    #    return b
    else:
		return gcd_Euclid(b, a%b)
		#gcd_Euclid(b, b%a)
		if False:		# mistakes. Using triple quotes cause indentation error
			if b > a:
				c = b-a
				if c <= b:
					return gcd_Euclid(c, b)
				else:
					return gcd_Euclid(a, c)
			else:
				c = a-b
				if c <= b:
					return gcd_Euclid(c, b)
				else:
					return gcd_Euclid(a, c)
			

print(gcd_Euclid(120, 2448))
