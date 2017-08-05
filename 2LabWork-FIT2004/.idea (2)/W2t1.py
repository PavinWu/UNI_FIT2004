def rec_fac(target):
    """
    recursive fac

    :param target:
    :return:
    """
    if target == 1:
        return 1
    return target * rec_fac(target-1)

if __name__ == "__main__":
    print(rec_fac(5))