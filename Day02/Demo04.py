# Auth: ShiHang
import copy
person = ['name',['salary',1000]]
person1 = person.copy()
person2 = person.copy()
person1[0] = 'shihang'
person2[0] = 'fangming'
print(person1)
print(person2)

person[1][1] = 50
print(person1)
print(person2)

