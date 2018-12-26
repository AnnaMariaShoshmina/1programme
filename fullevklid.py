def gcd(a,b):
    while b:
        a %= b
        a,b = b,a
    return a

def egcd(x,y):
    i = 0
    if y == 0:
        return 1, 0, gcd (x,y)
    x1,y1,i = egcd(y,x%y)
    return y1, x1 - x // y * y1, gcd (x,y)
    
print (egcd (21,35))
