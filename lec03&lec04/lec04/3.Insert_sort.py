#开始
#   |
#   V
#初始化，设置已排序部分只有第一个元素，未排序部分包括剩下的元素
#   |
#   V
#从未排序部分依次取出元素
#   |
#   V
#将取出的元素与已排序部分从后往前比较，找到合适的插入位置
#   |
#   V
#将元素插入到已排序部分的合适位置
#   |
#   V
#重复上述步骤，直到未排序部分为空
#   |
#   V
#结束，得到有序序列


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 测试代码
arr = [5, 2, 8, 12, 3]
insertion_sort(arr)
print("排序结果：", arr)
