import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取影像
image_path = "fisheye.jpg"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# 轉換為灰階影像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 二值化處理
_, binary = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

# 使用Sobel進行邊緣檢測
grad_x = cv2.Sobel(binary, cv2.CV_64F, 1, 0, ksize=11)
grad_y = cv2.Sobel(binary, cv2.CV_64F, 0, 1, ksize=11)
edges = cv2.magnitude(grad_x, grad_y)
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX)
edges = np.uint8(edges)

# 找到輪廓
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 找到最大輪廓
max_contour = max(contours, key=cv2.contourArea)

# 擬合圓
(x, y), radius = cv2.minEnclosingCircle(max_contour)
center = (int(x), int(y))
radius = int(radius)

# 繪製擬合圓和圓心
output_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
cv2.circle(output_image, center, radius, (0, 0, 255), 2)
cv2.circle(output_image, center, 5, (255, 0, 0), -1)  # 標出圓心

# 顯示每一步的結果
titles = ['Original Image', 'Grayscale Image', 'Binary Image', 'Edges (Sobel)', 'Fitted Circle']
images = [image, gray, binary, edges, output_image]

plt.figure(figsize=(20, 10))
for i in range(5):
    plt.subplot(2, 3, i + 1)
    if len(images[i].shape) == 2:
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')
plt.show()
