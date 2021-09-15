# Auth: ShiHang
print ("Hello World!")

name = input("姓名：")
age = input("年纪：")
job = input("职业：")

info = '''-----info of {_name}-----
name: {_name}
age: {_age}
job: {_job}'''.format(_name=name,
                    _age=age,
                    _job=job)

print(info)