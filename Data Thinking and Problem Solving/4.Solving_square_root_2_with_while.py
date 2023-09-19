guess = 1.0
epsilon = 0.0001  # 允许的误差范围

while True:
    difference = abs(guess * guess - 2)  # 计算当前猜测的平方与2之间的差值
    
    if difference <= epsilon:  
        break  
    
    guess = (guess + 2 / guess) / 2  # 使用牛顿迭代法更新猜测值

g = guess

print(g)  
