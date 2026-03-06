def read_input(filename):
    with open(filename) as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))
    return k, requests

import sys

if __name__ == "__main__":
    file = sys.argv[1]
    k, requests = read_input(file)

    print("k =", k)
    print("requests =", requests)