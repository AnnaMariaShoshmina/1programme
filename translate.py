def str_base (a,base):
    c = ""
    i = 0
    while base**i < a:
        i += 1
    d=a
    r=0
    i-=1
    while i >= 0:
        r= int (d/(base**i))
        if r <10:
            c += str (r)
        else:
            c += str (chr (65-10+r))
        d -= r*(base**i)
        i-=1
    return c
print(str_base(44027, 36))
