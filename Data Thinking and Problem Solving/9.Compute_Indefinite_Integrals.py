import random
import math

def f(x):
    return x**2 + 4*x*math.sin(x)

def montecarlo_integration(f, a, b, iterations):
    count_under_curve = 0

    for _ in range(iterations):
        x = random.uniform(a, b)
        y = random.uniform(0, max(f(a), f(b)))

        if y <= f(x):
            count_under_curve += 1

    area_under_curve = (count_under_curve / iterations) * (b - a)
    return area_under_curve

a = 2
b = 3
iterations = 1000000

integral_approx = montecarlo_integration(f, a, b, iterations)
print("定积分的近似值为:", integral_approx)
