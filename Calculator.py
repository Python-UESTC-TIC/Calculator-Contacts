# coding:UTF-8


# 加法函数
def add(x, y):
    return x + y


# 减法函数
def subtract(x, y):
    return x - y


# 乘法函数
def multiply(x, y):
    return x * y


# 除法函数
def divide(x, y):
    return x / y


while (1):

    # 用户输入
    print("请选择您需要选择运算：")
    print("1代表加法")
    print("2代表减法")
    print("3代表乘法")
    print("4代表除法")

    choice = input("请输入您的选择(1/2/3/4):")

    num1 = int(input("请输入第一个数字: "))
    num2 = int(input("请输入第二个数字: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("输入错误 ")
    print('按Enter键再次输入')
    input()




