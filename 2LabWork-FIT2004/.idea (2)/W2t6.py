def gcd_Euclid(a,b):
    if a>b:
        a, b = b, a
    print(a,b)

    if b == 0:
        return a
    #elif a == 0:
    #    return b
    else:
        """
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
        """
    gcd_Euclid(b, b%a)

print(gcd_Euclid(4, 8))