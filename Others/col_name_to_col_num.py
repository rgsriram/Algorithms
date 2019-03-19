def col_name_to_col_num(col_name):

    result = 0

    for col in col_name:
        result *= 26
        result += ord(col) - ord('A') + 1

    return result

print col_name_to_col_num('CB')