import sys
sys.setrecursionlimit(10**9)
import functools

lines = get_number()
generations = []
while lines>0:
    generations.append(get_number())
    lines-=1

memo = dict()
@functools.lru_cache(None)
def fibonacci(generation):
    if generation == 0:
        return 1
    elif generation == 1:
        return 1
    else:
        #change
        if (generation in memo):
            return memo[generation]
        memo[generation] = fibonacci(generation-1) + fibonacci(generation-2) % 10
        return memo[generation]

for generation in generations:
    print(fibonacci(generation)%10)
