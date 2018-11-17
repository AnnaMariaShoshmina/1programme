import functools
import math
@functools.lru_cache()
def is_simple_cached(value):
    flag = 1
    i = 2
    for i in range (int(math.sqrt(value))):
        if value % i:
            flag = 0
    return flag
print (is_simple_cached (217))
