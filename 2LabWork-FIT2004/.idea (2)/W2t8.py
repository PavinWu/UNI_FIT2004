def nth_fibonacci(Nth):
    """
    Get Nth number in the fibonacci series
    Implement with iterations

    pre_condition: N>=0
    :param N:
    :return:
    """
    a = 1
    b = 1
    count = 2
    while count < Nth:
        c = a + b
        a = b
        b = c
        count += 1

    print(c)

nth_fibonacci(12)
