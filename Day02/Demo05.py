# Auth: ShiHang
all_name = [['石杭','5000'],['方茗','10000']]
name = input("欢迎来到小方便利店，请输入你的账号名称：")
product_name = [['香烟',100],['茅台酒',3000],['打火机',10],['保健品',400],['dior',11000],['chanel',12000],['loewe',13000],['ysl',10001]]
length1 = len(all_name)
length2 = len(product_name)
list_product = []
num = 0
# print(all_name[num][0])
# print(name)
while num < length1:
    for item in all_name:
        if name == item[0]:
            print("您的账号余额还有", item[1])
            salary = int(item[1])
            print("-------商品列表-------")
            for index,item1 in enumerate(product_name):
                print(index,item1)
            print("退出购买，请输入：q")
            print("---------------------")
            while True:
                product_num = input("请输入您要购买的商品：")
                if product_num.isdigit():
                    product_num = int(product_num)
                    if int(product_num) < length2 and int(product_num) >= 0:
                        if salary < int(product_name[product_num][1]):
                            print("你的钱钱都不够啦，还买个毛线啊！")
                        else:
                            list_product.append(product_name[product_num])
                            salary -= int(product_name[product_num][1])
                            print("您本次购买的商品是",product_name[product_num])
                            print("您的余额是：",salary)
                            print("---------------------")
                    else:
                        print("您输入的商品序号不正确！")
                elif product_num == "q":
                    print("---------------------")
                    print("您购买的商品有：",list_product)
                    print("您的最终余额是：", salary)
                    print("---------------------")
                    exit()
                else:
                    print("您输入的商品序号不正确！")
        else:
            num += 1
    else:
        name = input("您输入的名字不正确，请重新输入！")
        num = 0


