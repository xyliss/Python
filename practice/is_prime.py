# 定义素数判定函数，参数num为待判定的正整数
def is_prime(num):
    # 小于2的数不是素数
    if num < 2:
        return False
    # 2是最小的素数
    if num == 2:
        return True
    # 偶数（除2外）都不是素数
    if num % 2 == 0:
        return False
    # 遍历从3到根号num的奇数，判断是否能整除
    max_divisor = int(num ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False
    # 所有条件都不满足，是素数
    return True

# 主程序：用户输入 + 函数调用 + 结果输出
if __name__ == "__main__":
    try:
        # 获取用户输入并转换为整数
        number = int(input("请输入一个正整数："))
        # 调用素数判定函数
        result = is_prime(number)
        # 打印结果
        if result:
            print(f"{number} 是素数")
        else:
            print(f"{number} 不是素数")
    # 处理非数字输入的异常
    except ValueError:
        print("输入错误！请输入有效的正整数")