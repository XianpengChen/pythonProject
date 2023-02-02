from random import randint


# 摇色子，默认摇两次
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


# 三个数相加，默认都是0
def add(a=0, b=0, c=0):
    return a + b + c


# 在参数名前面的*表示args是一个可变参数
def add_var(*args):
    total = 0
    for val in args:
        total += val
    return total


# 如果没有指定参数就使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))

print(add_var())
print(add_var(1))
print(add_var(1, 2))
print(add_var(1, 2, 3))
print(add_var(1, 3, 5, 7, 9))

# 对于任何一种编程语言来说，给变量、函数这样的标识符起名字都是一个让人头疼的问题，
# 因为我们会遇到命名冲突这种尴尬的情况。最简单的场景就是在同一个.py文件中定义了两个同名函数，
# 由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，
# 也就意味着两个函数同名函数实际上只有一个是存在的。
