

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)
    

def reku_incr(n=1):
    print(n)
    reku_incr(n+1)

reku_incr()


