str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1))  # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize())  # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())  # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper())  # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or'))  # 8
print(str1.find('shit'))  # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He'))  # False
print(str1.startswith('hel'))  # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))  # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, '*'))
print(str1.ljust(50, '*'))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

# 我们之前讲过，可以用下面的方式来格式化输出字符串。
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
# 当然，我们也可以用字符串提供的方法来完成字符串的格式，代码如下所示。
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
# Python 3.6以后，格式化字符串还有更为简洁的书写方式，
# 就是在字符串前加上字母f，我们可以使用下面的语法糖来简化上面的代码。
a, b = 5, 10
print(f'{a} * {b} = {a * b}')
