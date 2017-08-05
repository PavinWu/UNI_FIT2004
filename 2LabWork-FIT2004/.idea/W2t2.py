def itr_fac(target):
    """
    iterative factorial

    :param target:
    :return:
    """
    i = 1
    count = 1
    result = 1
    while count <= target:
        result *= i
        count += 1
        i += 1

    return result

print(itr_fac(5))