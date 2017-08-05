def print_all_primes(N):
    """
    print all primes from 1 to N
    :param N:
    :return:
    """
    for i in range(1,N+1):
        if is_prime(i):
            print(i)

def is_prime(p):
    if p < 1:
        return False
    elif p == 1:
        return False
    elif p == 2 or p == 3:
        return True
    elif p%2 == 0:
        return False
    else:
        for k in range(3, p, 2):
            if p%k == 0:
                return False
        return True

print_all_primes(200)
