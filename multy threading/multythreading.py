import threading, math

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    r = int(math.sqrt(n)) + 1
    for i in range(3, r, 2):
        if n % i == 0: return False
    return True

def check_numbers_parallel(nums):
    res = {}
    lock = threading.Lock()
    ts = []
    def w(x):
        p = is_prime(x)
        with lock:
            res[x] = p
    for x in nums:
        t = threading.Thread(target=w, args=(x,))
        ts.append(t); t.start()
    for t in ts:
        t.join()
    return res

if __name__ == "__main__":
    nums = [17,25,74,199,101,41,39,50,20,19,51]
    print(check_numbers_parallel(nums))

