import cv2

# 读取图片
image_path = r'D:\programing\Dase_intro\lec07\ch12\picture.jpg'
image = cv2.imread(image_path)

# 转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 指定调整后的大小（例如，调整为宽度为200像素，高度为150像素）
new_size = (200, 150)
resized_image = cv2.resize(gray_image, new_size)

# 保存结果
output_path = 'output_image.jpg'  # 保存处理后的图像的路径
cv2.imwrite(output_path, resized_image)

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Processed Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
