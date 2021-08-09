# Uses python3
import sys

d = {}

def fillCache(cache):
    for i in range(1, len(cache)):
        min_operation = cache[i-1] + 1 
        if i % 3 == 0:
            min_operation = min(cache[i // 3]  + 1, min_operation)
        elif i % 2 == 0:
            min_operation = min(cache[i // 2]  + 1, min_operation)
        cache[i] = min_operation

def optimal_operation(n):
    cache = [0] * (n + 1)
    fillCache(cache)
    last_cache_value = cache[-1] 
    result = [1] * last_cache_value  
    for i in reversed(range(1, last_cache_value)):
        result[i] = n
        if cache[n] == cache[n-1]+1:
            n -= 1
        elif (cache[n] == cache[n // 2]+1) and n % 2 == 0:
            n //= 2
        else: 
            n //= 3
    return result

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_operation(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
