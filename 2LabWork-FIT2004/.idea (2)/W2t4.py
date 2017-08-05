import math

def better_prime(N):
    """
    more efficient way to get prime numbers.

    Sieve if Eratosthenes
    """
    for i in range(1,N+1):
        if better_is_prime(i):
            print(i)

def better_is_prime(p):
    """
    http://stackoverflow.com/questions/5811151/why-do-we-check-upto-the-square-root-of-a-prime-number-to-determine-if-it-is-pri
    If (a > sqrt(n) and b > sqrt(n)) then a*b > sqrt(n)^2 == n
       (a < sqrt(n) and b < sqrt(n)) then a*b < sqrt(n)^2 == n
    therefore, either a or b is < sqrt(n).
    If n is not a prime, then it is a product of a and b.
    If n is a prime, then it has no a and b < n.
    Therefore, if there exits a factor of n (i.e. a or b) that is < sqrt(n), n is not a prime

    :param p:
    :return:
    """
    if p < 1:
        return False
    elif p == 1:
        return False
    elif p == 2 or p == 3:
        return True
    elif p%2 == 0:
        return False
    else:
        #print(int(p**(1/2)), end=" ")
        for k in range(3, int(p**(1/2))+1, 2): #Check "Up to" p**(1/2)
            if p%k == 0:
                return False
        return True

def sieve_prime(n):
    """
    Sieve of Eratosthenes implementation

    :param n:
    :return:
    """


#better_prime(200)

