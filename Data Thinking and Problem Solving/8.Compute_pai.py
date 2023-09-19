import math
import random

def calculate_pi_leibniz(iterations):
    pi_approx = 0
    sign = 1

    for i in range(iterations):
        term = sign / (2*i + 1)
        pi_approx += term
        sign *= -1

    pi_approx *= 4
    return pi_approx

iterations = 1000000
pi_approx_leibniz = calculate_pi_leibniz(iterations)
print("无穷级数法（莱布尼茨级数）计算π的近似值为:", format(pi_approx_leibniz, ".10f"))
print("与真实值π的差值为:", format(abs(math.pi - pi_approx_leibniz), ".10f"))



def calculate_pi_machin():
    pi_approx = 4 * (4*math.atan(1/5) - math.atan(1/239))
    return pi_approx

pi_approx_machin = calculate_pi_machin()
print("马青公式法（Machin公式）计算π的近似值为:", format(pi_approx_machin, ".10f"))
print("与真实值π的差值为:", format(abs(math.pi - pi_approx_machin), ".10f"))


def calculate_pi_montecarlo(iterations):
    count_inside_circle = 0

    for i in range(iterations):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            count_inside_circle += 1

    pi_approx = 4 * count_inside_circle / iterations
    return pi_approx

iterations = 1000000
pi_approx_montecarlo = calculate_pi_montecarlo(iterations)
print("蒙特卡洛法（Monte Carlo方法）计算π的近似值为:", format(pi_approx_montecarlo, ".10f"))
print("与真实值π的差值为:", format(abs(math.pi - pi_approx_montecarlo), ".10f"))
