import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取影像
image_path = "fisheye4.jpg"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# 轉換為灰階影像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 二值化處理
_, binary = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

# 創建新影像來存儲結果
filtered_image = np.zeros_like(binary)

# 找到由左到右的第一個白色點並保留
first_white_left_to_right = np.argmax(binary, axis=1)
for row in range(binary.shape[0]):
    col = first_white_left_to_right[row]
    if binary[row, col] == 255:
        filtered_image[row, col] = 255

# 找到由右到左的第一個白色點並保留
first_white_right_to_left = binary.shape[1] - np.argmax(np.fliplr(binary), axis=1) - 1
for row in range(binary.shape[0]):
    col = first_white_right_to_left[row]
    if binary[row, col] == 255:
        filtered_image[row, col] = 255

# 找到白色點的位置
white_points = np.argwhere(binary == 255)
mark_image=cv2.cvtColor(filtered_image,cv2.COLOR_GRAY2BGR)

# 找到最左邊和最右邊的白色點
leftmost_white_point = np.min(np.where(binary == 255)[1])
rightmost_white_point = np.max(np.where(binary == 255)[1])

# 計算白色點的重心
if len(white_points) > 0:
    cx = int(np.mean(white_points[:, 1]))  # 平均 x 座標
    cy = int(np.mean(white_points[:, 0]))  # 平均 y 座標
    
    # 計算重心到最左邊和最右邊白點的平均距離，作為圓的半徑
    distances_left = np.abs(cx - leftmost_white_point)
    distances_right = np.abs(cx - rightmost_white_point)
    radius = int((distances_left + distances_right) / 2)
    
    # 在影像上標示重心為藍色點，並以計算出的半徑畫圓
    cv2.circle(mark_image, (cx, cy), 5, (255, 0, 0), -1)  # 藍色圓點，半徑為 5
    cv2.circle(mark_image, (cx, cy), radius, (0, 0, 255), 2)  # 紅色圓線，半徑為計算出的平均距離

# 顯示所有處理結果在同一張圖上
plt.figure(figsize=(16, 12))

# 原始影像
plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Original Image')

# 灰階影像
plt.subplot(232)
plt.imshow(gray, cmap='gray')
plt.axis('off')
plt.title('Grayscale Image')

# 二值化後的影像
plt.subplot(233)
plt.imshow(binary, cmap='gray')
plt.axis('off')
plt.title('Binary Image after Thresholding')

# 找到的第一個白色點的結果
plt.subplot(234)
plt.imshow(filtered_image, cmap='gray')
plt.axis('off')
plt.title('Result of Finding First White Point')

# 帶有白色點重心標示的最終影像
plt.subplot(235)
plt.imshow(cv2.cvtColor(mark_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Final Image with Centroid Marked and Circle')

plt.tight_layout()
plt.show()
