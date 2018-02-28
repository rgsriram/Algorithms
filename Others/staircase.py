

def staircase(n):
    for i in range(n, 0, -1):

        for j in range((i-1), 0, -1):
            print ' ',

        for k in range(i, n+1):
            print '#',

        print


staircase(20)