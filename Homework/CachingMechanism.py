cache = {}
def square(n):
    if n in cache:
        print(f"Getting from cache for {n}")
        return cache[n]

    result = n * n
    cache[n] = result
    print(f"Computed and caching the result for {n}")
    return result


print(square(3))  # Computed and caching the result for 3
print(square(3))  # Getting from cache for 3
print(square(10))  # Computed and caching the result for 10
print(square(10))  # Getting from cache for 10