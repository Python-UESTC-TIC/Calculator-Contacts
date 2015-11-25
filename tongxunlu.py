a = {'张三':'18岁','QQ':123456789,'地址':'北京','email':'123456789@qq.com'}
b = {'李四':'15岁','QQ':475426959,'地址':'天津','email':'475426959@qq.com'}
c = {'王五':'17岁','QQ':939639365,'地址':'成都','email':'939639365@qq.com'}
d = {'赵六':'19岁','QQ':123456780,'地址':'南昌','email':'123456780@qq.com'}
name = str(input('请输入查找的名字：'))
if name in a:
    print(a)
elif name in b:
    print(b)
elif name in c:
    print(c)
elif name in d:
    print(d)
else:
    print('通讯录里没有这个人哦！')