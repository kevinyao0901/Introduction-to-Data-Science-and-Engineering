def cube_root(a, epsilon=1e-6):
    x = a  
    while True:
        y = (2*x + a/(x*x)) / 3  
        if abs(y - x) < epsilon:  
            break
        x = y  
    return x


a = int(input())
result = cube_root(a)
decimal_digits = "{:.5f}".format(result)
print(f"{a} 的三次方根: {decimal_digits}")