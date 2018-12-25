def repeat(n):
    def fun_function (tupai):
        def circle (x):
            ball = x
            for i in range (n):
                ball = tupai (ball)
            return (ball)
        return (circle)
    return (fun_function)

@repeat(2)
def plus_1(x):
    return x + 1


@repeat(0)
def mul_2(x):
    return x * 2

print(plus_1(3))  
print(mul_2(4))
            
