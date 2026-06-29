import math


def calculate_pizza_num():
    """计算大披萨等价替换的小披萨最小个数"""
    print("===== 披萨尺寸等价替换计算器 =====")
    # 循环实现多次计算，输入q退出
    while True:
        try:
            # 提示用户输入，支持退出指令
            m_input = input("\n请输入大披萨的尺寸（英寸），输入q退出：")
            if m_input.lower() == "q":
                print("程序已退出！")
                break

            n_input = input("请输入小披萨的尺寸（英寸）：")
            if n_input.lower() == "q":
                print("程序已退出！")
                break

            # 转换为浮点型，支持非整数尺寸（如8.5英寸）
            m_size = float(m_input)
            n_size = float(n_input)

            # 验证尺寸是否为正数
            if m_size <= 0 or n_size <= 0:
                print("错误：披萨尺寸必须为正数！请重新输入。")
                continue

            # 计算面积比值（直径平方比）
            area_ratio = m_size ** 2 / n_size ** 2
            # 向上取整得到最小个数
            min_num = math.ceil(area_ratio)

            # 格式化输出结果，清晰直观
            print(f"\n【计算结果】")
            print(f"大披萨尺寸：{m_size} 英寸，小披萨尺寸：{n_size} 英寸")
            print(f"面积比值（大/小）：{area_ratio:.2f}")
            print(f"至少需要 {min_num} 个 {n_size} 英寸的小披萨，顾客才不吃亏。")

        # 捕获非数字输入的异常
        except ValueError:
            print("错误：请输入有效的数字（或q退出）！")
        # 捕获其他未知异常
        except Exception as e:
            print(f"程序出错：{e}，请重新尝试。")


# 调用函数执行程序
if __name__ == "__main__":
    calculate_pizza_num()