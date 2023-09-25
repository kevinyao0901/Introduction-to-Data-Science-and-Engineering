import random
import time

# 生成指定长度的随机整数列表
def generate_random_list(length):
    return [random.randint(0, 1000) for _ in range(length)]

# 选择排序算法
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

# 归并排序算法
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

# 测试不同长度数列下的排序算法运行时间
lengths = [100, 500, 1000, 5000, 10000]

for length in lengths:
    array = generate_random_list(length)

    start_time = time.time()
    selection_sort(array)
    end_time = time.time()
    selection_sort_time = end_time - start_time

    start_time = time.time()
    merge_sort(array)
    end_time = time.time()
    merge_sort_time = end_time - start_time

    print("长度为 {} 的随机数列：".format(length))
    print("选择排序的运行时间：{:.5f} 秒".format(selection_sort_time))
    print("归并排序的运行时间：{:.5f} 秒".format(merge_sort_time))
    print()
