# Auth: ShiHang
import getpass
_username = "shihang"
_passwd = "shihang"
username = input("username:")
password = input("password:")

if _username == username and _passwd == password:
    print("Welcome user {name} login".format(name=username))
else:
    print("Invalid Username and Password!")

print(username,password)

