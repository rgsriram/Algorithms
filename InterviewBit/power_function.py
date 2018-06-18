"""
int pow(int x, int n, int d) {
        int result = 1;
        int square = x;
        if(x == 0)
            return 0;
        if(n == 0)
            return 1;
        while(n != 0){
            if(n % 2 != 0){
                result = result *  square;
            }
            square = (square * square) % d;
            n = n/2;
            if(result > d)
                result = result % d;
        }
        System.out.println(result);
        System.out.println((result + d) % d);
        return result;
    }
"""


def pow(x, n, d):
    if not x:
        return 0

    if not n:
        return 1

    a = 1
    y = x % d

    if y < 0:
        y += d

    while n > 0:
        if n & 1:
            a = (a * y) % d

        y *= y
        y %= d

        if y < 0:
            y += d

        n = n >> 1

    return int(a)

print pow(-3, 3, 5)



"""
    if(x==0)
        return 0;
    if(n==0)
        return 1;
    long long a=1;
    long long y=x%d;
    if(y<0) y=y+d;
    while(n>0){
        if(n&1){
            a=(a*y)%d;
        }
        y=y*y;
        y=y%d;
        if(y<0)
            y+=d;
        n=n>>1;
    }
    return (int)a;
}
"""
