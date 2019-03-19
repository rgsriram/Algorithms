def col_num_to_col_name(num):
    string = []

    while num > 0:
        rem = num % 26

        if rem == 0:
            string.append('Z')
            num = (num/26) - 1

        else:
            string.append(chr((rem-1) + ord('A')))
            num /= 26

    string = string[::-1]

    return "".join(string)

print col_num_to_col_name(80)