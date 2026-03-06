def read_input(filename):
    with open(filename) as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))
    return k, requests

from collections import deque

def fifo(k, requests):
    cache = set()
    queue = deque()
    misses = 0

    for r in requests:
        if r not in cache:
            misses += 1
            if len(cache) == k:
                old = queue.popleft()
                cache.remove(old)
            cache.add(r)
            queue.append(r)
    return misses

import sys

if __name__ == "__main__":
    file = sys.argv[1]
    k, requests = read_input(file)

    print("k =", k)
    print("requests =", requests)
    print("FIFO:", fifo(k, requests))