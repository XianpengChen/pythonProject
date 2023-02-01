# 输入一个正整数判断它是不是素数
from math import sqrt

number = int(input('请输入一个正整数：'))
end = int(sqrt(number))
is_prime = True
for x in range(2, end + 1):
    if number % x == 0:
        is_prime = False
        break
if is_prime and number != 1:
    print('%d是素数' % number)
else:
    print('%d不是素数' % number)
