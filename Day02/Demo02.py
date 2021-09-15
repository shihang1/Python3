# Auth: ShiHang
msg = "我爱北京天安门！"
print("msg:",msg)

# print(msg.encode())

msg1=msg.encode("utf-8")
print("msg1:",msg1)

msg2=msg1.decode("utf-8")
print("msg2:",msg2)