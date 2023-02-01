# 生成斐波那契数列的前20个数。
# 斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .。
intA = 1
intB = 1
print(intA, end=' ')
print(intB, end=' ')
curr = 0
for x in range(3, 21):
    curr = intA + intB
    intA = intB
    intB = curr
    print(curr, end=' ')


