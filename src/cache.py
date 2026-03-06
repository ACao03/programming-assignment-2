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

from collections import OrderedDict

def lru(k, requests):
    cache = OrderedDict()
    misses = 0

    for r in requests:
        if r in cache:
            cache.move_to_end(r)
        else:
            misses += 1
            if len(cache) == k:
                cache.popitem(last=False)
        cache[r] = True
    return misses

def otpff(k, requests):
    cache = set()
    misses = 0

    for i in range(len(requests)):
        r = requests[i]
        if r in cache:
            continue
        misses += 1
        if len(cache) < k:
            cache.add(r)
        else:
            farthest = -1
            victim = None
            for c in cache:
                try:
                    next_use = requests.index(c, i + 1)
                except ValueError:
                    next_use = float('inf')
                if next_use > farthest:
                    farthest = next_use
                    victim = c
            cache.remove(victim)
            cache.add(r)
    return misses

import sys

if __name__ == "__main__":
    file = sys.argv[1]
    k, requests = read_input(file)

    print("k =", k)
    print("requests =", requests)
    print("FIFO  :", fifo(k, requests))
    print("LRU   :", lru(k, requests))
    print("OPTFF :", optff(k, requests))