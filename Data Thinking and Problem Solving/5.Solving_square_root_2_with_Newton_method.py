def f(x):
    return x**2 - 2

def f_prime(x):
    return 2*x

guess = 2.0

for i in range(10):
    f_guess = f(guess)
    f_prime_guess = f_prime(guess)
    
    guess = guess - f_guess / f_prime_guess

g = guess
print(g)

guess = 2000.0
for i in range(10):
    f_guess = f(guess)
    f_prime_guess = f_prime(guess)
    
    guess = guess - f_guess / f_prime_guess
    
g = guess
print(g)
