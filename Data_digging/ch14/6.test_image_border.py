import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread("D:\programing\Dase_intro\lec08\ch14\mango_sherbet.jpg", cv2.IMREAD_GRAYSCALE)

# 定义垂直边缘检测的Sobel卷积核
sobel_kernel = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])

# 使用滤波器进行卷积
edge_image = cv2.filter2D(image, -1, sobel_kernel)

# 显示原始图像和垂直边缘检测结果
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('original'), plt.axis('off')
plt.subplot(122), plt.imshow(edge_image, cmap='gray')
plt.title('edge detection'), plt.axis('off')
plt.show()
