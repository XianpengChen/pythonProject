# 打印三角形图案
row = int(input('请输入行数：'))

# 为末尾end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串，其实这也是一个语法要求，表示这个语句没结束。
for i in range(row):
    # "_"是一个循环标志，类似于普通变量，只是不取值，只循环
    for _ in range(i+1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
