# 在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，
# 如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，下面的代码可以验证这一点。
class Test(object):
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)


# 在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。
# 所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，
# 本类之外的代码在访问这样的属性时应该要保持慎重。
if __name__ == '__main__':
    main()
