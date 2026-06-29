# 定义计算器函数，参数：数字1、数字2、运算符
def calculate(num1, num2, op):
    # 加法运算
    if op == "+":
        return num1 + num2
    # 减法运算
    elif op == "-":
        return num1 - num2
    # 乘法运算
    elif op == "*":
        return num1 * num2
    # 除法运算（判断除零错误）
    elif op == "/":
        if num2 == 0:
            return "错误：除数不能为0"
        return num1 / num2
    # 非法运算符
    else:
        return "错误：请输入有效运算符(+ - * /)"


# 主程序：用户输入 + 函数调用 + 格式化输出
if __name__ == "__main__":
    try:
        # 获取用户输入
        n1 = float(input("请输入第一个数字："))
        operator = input("请输入运算符(+ - * /)：")
        n2 = float(input("请输入第二个数字："))

        # 调用计算器函数
        res = calculate(n1, n2, operator)

        # 格式化打印计算式和结果
        print(f"{n1} {operator} {n2} = {res}")
    # 处理非数字输入异常
    except ValueError:
        print("输入错误！请输入有效的数字")