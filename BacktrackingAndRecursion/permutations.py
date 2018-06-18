import copy

a = [1, 2, 3]


class t:
    def __init__(self):
        self.li = []

    def permute(self, a, l, r, k):

        if l == r:
            k.append(copy.copy(a))
            return k

        else:

            for i in range(l, r+1):
                a[l], a[i] = a[i], a[l]
                self.permute(a, l+1, r, k)
                print l, i

                a[l], a[i] = a[i], a[l]

                print a

        print '\n'

        return k

x = t()
x.permute(a, 0, len(a)-1, [])
