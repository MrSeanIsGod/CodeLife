import numpy as np
import cv2

def Sobel_gradient(f, direction):
    sobel_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    sobel_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    if direction == 1:
        grad_x = cv2.filter2D(f, cv2.CV_32F, sobel_x)
        gx = np.uint8(np.clip(abs(grad_x), 0, 255))
        return gx
    elif direction == 2:
        grad_y = cv2.filter2D(f, cv2.CV_32F, sobel_y)
        gy = np.uint8(np.clip(abs(grad_y), 0, 255))
        return gy
    else:
        grad_x = cv2.filter2D(f, cv2.CV_32F, sobel_x)
        grad_y = cv2.filter2D(f, cv2.CV_32F, sobel_y)
        magnitude = abs(grad_x) + abs(grad_y)
        g = np.uint8(np.clip(magnitude, 0, 255))
        return g

def main():
    img = cv2.imread("gray_image.jpg", -1)
    gx = Sobel_gradient(img, 1)
    gy = Sobel_gradient(img, 2)
    g = Sobel_gradient(img, 3)

    cv2.imshow("Original Image", img)
    cv2.imshow("Gradient in x", gx)
    cv2.imshow("Gradient in y", gy)
    cv2.imshow("Gradient", g)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()