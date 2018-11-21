import functools
import math
@functools.lru_cache()
def is_simple_cached(value):
    for i in range (2, 1+math.ceil(math.sqrt(value))):
        if value % i == 0:
            return False
    return True
for i in range(1,100):
    print (i,is_simple_cached (i))
