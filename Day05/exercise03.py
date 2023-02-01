# 输出100以内所有的素数。素数指的是只能被1和自身整除的正整数（不包括1）。
from math import sqrt

for x in range(2, 101):
    root = int(sqrt(x))
    is_prime = True
    for i in range(1, root + 1):
        if x % i == 0 and i != 1:
            is_prime = False
            break
    if is_prime:
        print(x, end=' ')