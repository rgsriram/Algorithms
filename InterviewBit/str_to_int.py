def str_to_int(st):
    number = 0

    for each in st:
        number = (number * 10) + (ord(each) - 48)

    print number


str_to_int('00123')


