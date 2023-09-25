def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"

    integer_part = int(decimal)
    fractional_part = abs(decimal - integer_part)

    binary_integer = ""
    while integer_part > 0:
        remainder = integer_part % 2
        binary_integer = str(remainder) + binary_integer
        integer_part = integer_part // 2

    binary_fractional = ""
    precision = 16  # 设置小数部分的精度
    while fractional_part > 0 and len(binary_fractional) <= precision:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit

    if decimal < 0:
        return "-" + binary_integer + "." + binary_fractional
    else:
        return binary_integer + "." + binary_fractional

decimal_input = float(input("请输入十进制数："))
binary_output = decimal_to_binary(decimal_input)
print("二进制数为:", binary_output)
