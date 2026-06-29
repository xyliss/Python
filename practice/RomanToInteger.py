# 罗马数字转十进制整数
# 1. 定义罗马数字与整数的映射字典（组合数据类型：字典）
roman_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

# 2. 获取用户输入并标准化为大写
roman_str = input("请输入罗马数字：").strip().upper()

# 3. 初始化结果与遍历索引
result = 0
index = 0

# 4. 遍历罗马数字字符串并计算
while index < len(roman_str):
    # 判断当前两位是否为特殊组合
    if index + 1 < len(roman_str) and roman_str[index:index+2] in roman_map:
        result += roman_map[roman_str[index:index+2]]
        index += 2
    else:
        result += roman_map[roman_str[index]]
        index += 1

# 5. 输出最终结果
print("对应的十进制整数：", result)