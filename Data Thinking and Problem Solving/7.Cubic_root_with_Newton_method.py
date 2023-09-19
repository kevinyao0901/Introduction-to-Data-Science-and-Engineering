def f(x):
    return x**3 - c

def f_prime(x):
    return 3 * x**2

def newton_cuberoot(c):
    guess = c / 2

    for i in range(10):
        f_guess = f(guess)
        f_prime_guess = f_prime(guess)

        guess = guess - f_guess / f_prime_guess

    return guess

c = 10
result = newton_cuberoot(c)
print("c的三次方根为:", result)
