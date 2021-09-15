# Auth: ShiHang
#The game of guess age

_age = 32

age = int(input("请输入你猜测的年龄："))

if age == _age:
    print("你猜测正确了！")
elif age > _age:
    print("你猜测的年龄太大了！")
else:
    print("你猜测的年龄偏小了！")