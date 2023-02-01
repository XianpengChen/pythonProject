# 输入两个正整数计算它们的最大公约数和最小公倍数
int1 = int(input('请输入正整数1：'))
int2 = int(input('请输入正整数2：'))

# 如果int1大于int2就交换int1和int2的值
if int1 > int2:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    int1, int2 = int2, int1
# 从两个数中较小的数开始做递减的循环
for max_factor in range(int1, 0, -1):
    if int1 % max_factor == 0 and int2 % max_factor == 0:
        print('%d和%d的最大公约数是%d' % (int1, int2, max_factor))
        print('%d和%d的最小公倍数是%d' % (int1, int2, int1 * int2 // max_factor))
        break

