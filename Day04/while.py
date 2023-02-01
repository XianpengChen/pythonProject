import random
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('你猜对了!')
        break
print('你一共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
# 上面的代码中使用了break关键字来提前终止循环，需要注意的是break只能终止它所在的那个循环
