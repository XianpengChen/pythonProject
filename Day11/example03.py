"""那么这里还有一个问题，如果希望把一个列表或者一个字典中的数据保存到文件中又该怎么做呢？
答案是将数据以JSON格式进行保存。我们使用Python中的json模块就可以将字典或列表以JSON格式保存到文件中，代码如下所示。"""
import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')

    with open('data.json', 'r', encoding='utf-8') as fs:
        dict2 = json.load(fs)
        print(dict2)


if __name__ == '__main__':
    main()
