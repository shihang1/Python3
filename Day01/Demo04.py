# Auth: ShiHang
'''
count = 0
while count <= 10:
    print("count:",count)
    count = count +1


age = 32
_age = int(input("请输入你猜测的年龄："))
while _age != 32:
    if _age < age:
        print("你猜的年纪偏小，请继续猜测！")
        _age = int(input("请输入你猜测的年龄："))
    else:
        print("你猜的年纪偏大,请继续猜测!")
        _age = int(input("请输入你猜测的年龄："))

print("你猜测正确啦！")
print("正确的年龄是：",age)
'''

age = 55
count = 0

while count < 3:
    _age = int(input("请输入你猜测的年龄："))
    if age == _age:
        print("你猜测正确了！")
        break
    elif age < _age:
        print("你猜测的年龄太大了！")
    else:
        print("你猜测的年龄偏小了！")
    count +=1
else:
    print("你尝试次数过多了！")