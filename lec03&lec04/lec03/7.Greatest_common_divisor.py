def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = int(input("请输入第一个正整数："))
num2 = int(input("请输入第二个正整数："))

result = gcd(num1, num2)

print("{} 和 {} 的最大公约数是：{}".format(num1, num2, result))
