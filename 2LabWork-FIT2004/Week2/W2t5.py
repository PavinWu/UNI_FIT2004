def gcd(a,b):
    """
    Compute Greatest Common divisor (GCD) of a and b
    :param a:
    :param b:
    :return:
    """
    factor_list = []
    # common factor is the factor of n than can be square rooted
    # gcd is the product of the common factors
    n = a*b
    n_temp = n
    while n_temp > 1:
        i = 2   #1 is always a factor
        factor_found = False
        while not factor_found:
            if n_temp % i == 0:
                factor_list.append(i)
                n_temp /= i
                print(i)
                factor_found = True
            i += 1

    # find if factor has a duplicate
    # (you will always get a prime result since the factor that is larger than prime will not be encountered)
    # Therefore, we don't have to worry about duplicated number being divisible (e.g. 4*4)
    factor_list_dup = []
    while len(factor_list) > 0:
        dup_found = False
        #while not dup_found:

def gcd_easier(a,b):
    # you don't have to decompose!!
    if a > b:
        test = a
    else:
        test = b
    gcd_found = False
    while test > 0 and not gcd_found:
        if(a % test == 0 and b % test == 0):
            gcd_found = True
            return test
        test -= 1

print(gcd_easier(4,8))
