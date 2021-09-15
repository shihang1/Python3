# Auth: ShiHang
f = open("test1.txt",'r',encoding="utf-8")   #复制给f内存对象，文件句柄,r读模式打开,w写模式，a追加模式,
#这三个模式单独存在都不能读
# m = open("test.txt",encoding="utf-8")
# # data = f.read()
# # data2 = f.read()  #接着data继续读，读完一边没有了
# # print(data)
# # print("---------")#读文件
# # print(data2)
#
# f.write("我是第六行！\n")
# # data = f.read()
# # print(data)
#
# f.close()

#print(f.readlines())  #生产列表
# for line in f.readlines():
#     print(line)
    #print(line.strip())  #去除空格换行
# print("---------")
# print(f.readline())    #只适合读小文件
# print("---------")
# print(f.readline())
# for i in range(5):
#     print(f.readline())

#第三行不打印，low循环
# for index,line in enumerate(f.readlines()):
#     if index == 2:
#         print("--我是第三行--")
#         continue
#     print(line.strip())
count = 0
#效率高的读，一行一行读
for line in f:  #将文件变成迭代器
    if count == 2:
        print("--我是第三行--")
        count += 1
        continue
    print(line.strip())
    count +=1