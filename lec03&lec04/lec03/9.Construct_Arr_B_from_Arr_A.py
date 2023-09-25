def construct_array(A):
    n = len(A)
    left_product = [1] * n
    right_product = [1] * n

    # 计算左侧乘积
    for i in range(1, n):
        left_product[i] = left_product[i-1] * A[i-1]

    # 计算右侧乘积
    for i in range(n-2, -1, -1):
        right_product[i] = right_product[i+1] * A[i+1]

    # 计算数组B
    B = [left_product[i] * right_product[i] for i in range(n)]

    return B



A=[1,2,3,4,5]
print(construct_array(A))