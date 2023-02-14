"""在Python中实现文件的读写操作其实非常简单，通过Python内置的open函数，
我们可以指定文件名、操作模式、编码信息等来获得操作文件的对象，接下来就可以对文件进行读写操作了。
这里所说的操作模式是指要打开什么样的文件（字符文件还是二进制文件）以及做什么样的操作（读、写还是追加），具体的如下表所示。"""
import time


def main():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='UTF-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


"""如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，
通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源，
代码如下所示。"""


def main1():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


"""除了使用文件对象的read方法读取文件之外，
还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中，
代码如下所示。"""


def main_loop():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('致橡树.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('致橡树.txt', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main_loop()
