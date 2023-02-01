# 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$
for number in range(100, 1000):
    low = number % 10
    mid = number // 10 % 10
    high = number // 100
    if number == low ** 3 + mid ** 3 + high ** 3:
        print(number)

# 正整数的反转 例如：将12345变成54321
num = int(input('请输入一个正整数：'))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
print(reverse_num)

