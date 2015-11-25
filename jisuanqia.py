#这个还是借鉴的(。・_・)/~~~
#定义加法
def jiafa(x,y):
    return x + y

#定义减法
def jianfa(x,y):
    return x - y

#定义乘法
def chengfa(x,y):
    return x * y
	
#定义除法
def chufa(x,y):
    return x / y
	
while 1:
    print("我是低级程序，只能计算两个数字哦~")
    print("加减乘除分别对应1、2、3、4")
    leixing = int(input("请输入您的选择"))
    a = int(input("请输入第一个数字:"))
    b = int(input("请输入第二个数字:"))
    if leixing == 1:
        print(jiafa(a,b))
    elif leixing == 2:
        print(jianfa(a,b))
    elif leixing == 3:
        print(chengfa(a,b))
    elif leixing == 4:
        print(chufa(a,b))
    else:
        print("不能输入其他数字哦~")
    print("按enter键继续")
    input()