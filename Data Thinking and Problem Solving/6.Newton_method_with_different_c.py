def f(x):
    return x**2 - 2

def f_prime(x):
    return 2*x

# 初始猜测值为 c
def newton_sqrt(c):
    guess = c

    for i in range(10):
        f_guess = f(guess)
        f_prime_guess = f_prime(guess)

        guess = guess - f_guess / f_prime_guess

    return guess

c = 2
result1 = newton_sqrt(c)
print("初始猜测值为 c，结果为:", result1)

# 初始猜测值为 c/4
def newton_sqrt_v2(c):
    guess = c / 4

    for i in range(10):
        f_guess = f(guess)
        f_prime_guess = f_prime(guess)

        guess = guess - f_guess / f_prime_guess

    return guess

result2 = newton_sqrt_v2(c)
print("初始猜测值为 c/4，结果为:", result2)

