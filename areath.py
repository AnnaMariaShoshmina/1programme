import math

iterations = 20

def my_atanh(x):
    x_pow = x
    for n in range (1, iterations):
        x_pow +=(x**(2*n+1))/(2*n+1)
    return x_pow
print(help(math.atanh),math.atanh(0.4))
print(help(my_atanh), my_atanh(0.4))
