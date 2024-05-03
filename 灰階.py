import cv2

# 讀取圖片
image_path = "irregular_480.jpg"  # 替換成你的圖片路徑
image = cv2.imread(image_path)

# 檢查圖片是否成功讀取
if image is None:
    print("無法讀取圖片。請確保圖片路徑正確。")
else:
    # 將圖片轉換為灰階
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 保存灰階圖片
    cv2.imwrite("gray_image.jpg", gray_image)  # 儲存為gray_image.jpg

    # 顯示灰階圖片（可選）
    cv2.imshow("Gray Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()