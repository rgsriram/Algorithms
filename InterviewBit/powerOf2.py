def is_powerOfTwo(num):

    if num == 0:
        return False

    if num == 1:
        return True

    return not (num & num-1)