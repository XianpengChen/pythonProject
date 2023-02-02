# 输入M和N计算C(M,N)

def fac(number):
    result = 1
    for n in range(1, number + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m - n))
