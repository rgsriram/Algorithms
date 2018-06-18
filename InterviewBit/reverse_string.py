def reverse(str):
    start_index = 0
    i = 0
    j = len(str)
    st = []

    while i < j:

        if str[i] == ' ':

            if start_index == i:
                i += 1
                start_index = i
                continue

            st.append(str[start_index:i])
            start_index = i + 1

        i += 1

    st.append(str[start_index:j])
    return st

res = reverse('the sky is blue')

print ' '.join(reversed(res))

