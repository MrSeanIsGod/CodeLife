import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, 
                             QPushButton, QComboBox, QSlider, QFileDialog, QWidget)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

class ImageProcessor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        self.image = None
        self.processed_image = None

    def initUI(self):
        #初始化使用者介面
        self.setWindowTitle('Image Processing GUI')
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        
        # 添加下拉選單
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Original")
        self.comboBox.addItem("Grayscale")
        self.comboBox.addItem("Sobel Edge Detection")
        self.comboBox.addItem("Laplacian Edge Detection")
        self.comboBox.addItem("Canny Edge Detection")
        self.comboBox.addItem("Sharpen")
        self.comboBox.addItem("HSV")
        self.comboBox.addItem("Gaussian Blur")
        self.comboBox.addItem("Binary Threshold")
        self.comboBox.addItem("Random Rotation")
        self.comboBox.currentIndexChanged.connect(self.apply_effect)
        
        # 添加滑動條
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.apply_effect)
        
        # 添加HSV滑動條
        self.slider_h = QSlider(Qt.Horizontal, self)
        self.slider_h.setMinimum(0)
        self.slider_h.setMaximum(180)
        self.slider_h.setValue(0)
        self.slider_h.valueChanged.connect(self.apply_effect)
        
        self.slider_s = QSlider(Qt.Horizontal, self)
        self.slider_s.setMinimum(0)
        self.slider_s.setMaximum(255)
        self.slider_s.setValue(0)
        self.slider_s.valueChanged.connect(self.apply_effect)
        
        self.slider_v = QSlider(Qt.Horizontal, self)
        self.slider_v.setMinimum(0)
        self.slider_v.setMaximum(255)
        self.slider_v.setValue(0)
        self.slider_v.valueChanged.connect(self.apply_effect)
        
        # 添加滑動條標籤
        self.slider_label_h = QLabel('Hue: 0', self)
        self.slider_label_s = QLabel('Saturation: 0', self)
        self.slider_label_v = QLabel('Value: 0', self)
        
        self.slider_label = QLabel('Value:', self)
        
        # 添加儲存按鈕
        self.saveButton = QPushButton('Save', self)
        self.saveButton.clicked.connect(self.save_image)
        
        # 佈局
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.comboBox)
        layout.addWidget(self.slider)
        layout.addWidget(self.slider_h)
        layout.addWidget(self.slider_s)
        layout.addWidget(self.slider_v)
        layout.addWidget(self.slider_label_h)
        layout.addWidget(self.slider_label_s)
        layout.addWidget(self.slider_label_v)        
        layout.addWidget(self.slider_label)
        layout.addWidget(self.saveButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # 根據所選效果更新滑動條顯示
        self.comboBox.currentIndexChanged.connect(self.update_slider_visibility)
        self.update_slider_visibility()

        self.show()

    def load_image(self, file_path):
        # 載入影像
        self.image = cv2.imread(file_path)
        self.processed_image = self.image.copy()
        self.display_image(self.image)

    def display_image(self, image):
        # 顯示影像
        qformat = QImage.Format_Indexed8 if len(image.shape) == 2 else QImage.Format_RGB888
        image = QImage(image.data, image.shape[1], image.shape[0], image.strides[0], qformat)
        image = image.rgbSwapped()
        self.image_label.setPixmap(QPixmap.fromImage(image))

    def apply_effect(self):
        # 應用影像效果
        if self.image is None:
            return

        effect = self.comboBox.currentText()
        value = self.slider.value()

        if effect == "Original":
            self.processed_image = self.image.copy()
            self.slider_label.setText('Value:')
        elif effect == "Grayscale":
            self.processed_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.slider_label.setText('Value:')
        elif effect == "Sobel Edge Detection":
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
            sobelx = cv2.convertScaleAbs(sobelx)
            sobely = cv2.convertScaleAbs(sobely)
            self.processed_image = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
            self.slider_label.setText('Value:')
        elif effect == "Laplacian Edge Detection":
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            laplacian = cv2.Laplacian(gray, cv2.CV_64F)
            self.processed_image = cv2.convertScaleAbs(laplacian)
            self.slider_label.setText('Value:')
        elif effect == "Canny Edge Detection":
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.processed_image = cv2.Canny(gray, value, value * 2)
            self.slider_label.setText(f'Threshold: {value}')
        elif effect == "Sharpen":
            alpha = value / 50.0
            kernel = np.array([[-1, -1, -1],
                               [-1,  9, -1],
                               [-1, -1, -1]]) * alpha
            self.processed_image = cv2.filter2D(self.image, -1, kernel)
            self.slider_label.setText(f'Alpha: {alpha:.2f}')
        elif effect == "HSV":
            h, s, v = cv2.split(cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV))
            h = np.clip(h + self.slider_h.value(), 0, 179)
            s = np.clip(s + self.slider_s.value(), 0, 255)
            v = np.clip(v + self.slider_v.value(), 0, 255)
            self.processed_image = cv2.cvtColor(cv2.merge((h, s, v)), cv2.COLOR_HSV2BGR)
            self.slider_label_h.setText(f'Hue: {self.slider_h.value()}')
            self.slider_label_s.setText(f'Saturation: {self.slider_s.value()}')
            self.slider_label_v.setText(f'Value: {self.slider_v.value()}')
        elif effect == "Gaussian Blur":
            ksize = (value // 5) * 2 + 1
            self.processed_image = cv2.GaussianBlur(self.image, (ksize, ksize), 0)
            self.slider_label.setText(f'Kernel Size: {ksize}x{ksize}')
        elif effect == "Binary Threshold":
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            _, self.processed_image = cv2.threshold(gray, value, 255, cv2.THRESH_BINARY)
            self.slider_label.setText(f'Threshold: {value}')
        elif effect == "Random Rotation":
            angle = value * 3.6  # Value in degrees (0-360)
            h, w = self.image.shape[:2]
            M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)
            self.processed_image = cv2.warpAffine(self.image, M, (w, h))
            self.slider_label.setText(f'Angle: {angle:.1f}°')
        self.display_image(self.processed_image)

    def save_image(self):
        # 儲存影像
        if self.processed_image is not None:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png);;JPG Files (*.jpg);;All Files (*)")
            if file_path:
                # 如果影像不是RGB格式，轉換為RGB格式
                if len(self.processed_image.shape) == 3 and self.processed_image.shape[2] == 3:
                    processed_image_rgb = self.processed_image
                else:
                    processed_image_rgb = cv2.cvtColor(self.processed_image, cv2.COLOR_BGR2RGB)
                
                # 儲存影像
                cv2.imwrite(file_path, processed_image_rgb)



    def update_slider_visibility(self):
        # 更新滑動條的可見性
        effect = self.comboBox.currentText()
        if effect in ["Canny Edge Detection", "Sharpen", "Gaussian Blur", "Binary Threshold", "Random Rotation"]:
            self.slider.show()
            self.slider_h.hide()
            self.slider_s.hide()
            self.slider_v.hide()
            self.slider_label.show()
            self.slider_label_h.hide()
            self.slider_label_s.hide()
            self.slider_label_v.hide()            
        elif effect in ["HSV"]:
            self.slider.hide()
            self.slider_h.show()
            self.slider_s.show()
            self.slider_v.show()
            self.slider_label.hide()
            self.slider_label_h.show()
            self.slider_label_s.show()
            self.slider_label_v.show()            
        else:
            self.slider.hide()
            self.slider_h.hide()
            self.slider_s.hide()
            self.slider_v.hide()
            self.slider_label.hide()
            self.slider_label_h.hide()
            self.slider_label_s.hide()
            self.slider_label_v.hide()            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageProcessor()
    file_path, _ = QFileDialog.getOpenFileName(ex, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
    if file_path:
        ex.load_image(file_path)
    sys.exit(app.exec_())

       
