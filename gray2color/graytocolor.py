import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

monkey_RGB=cv2.imread("monkey.jpg")
monkey_gray=cv2.cvtColor(monkey_RGB, cv2.COLOR_BGR2GRAY)
monkey_pseudo=cv2.cvtColor(monkey_gray, cv2.COLOR_GRAY2RGB)
cv2.imshow("RGB", monkey_RGB)
cv2.imshow("Gray", monkey_gray)
cv2.imshow("Pseudo", monkey_pseudo)

N=20
fig2=plt.figure(2)
colors = [(np.sin(r), np.sin(g), np.sin(b)) for (r, g, b) in zip(np.linspace(2*np.pi, 0, N), \
                                                                  np.linspace(0, np.pi, N), \
                                                                  np.linspace(0, 2*np.pi, N))]
my_cmap=mpl.colors.ListedColormap (colors)

plt.imshow(monkey_gray, cmap=my_cmap)

red_wave = np.sin(np.linspace(2*np.pi, 0, N))
green_wave = np.sin(np.linspace(0, np.pi, N))
blue_wave = np.sin(np.linspace(0, 2*np.pi, N))

plt.figure(figsize=(10, 5))
plt.plot(red_wave, color='red', label='Red')
plt.plot(green_wave, color='green', label='Green')
plt.plot( blue_wave, color='blue', label='Blue')
plt.title('RGB Channel Waves')
plt.xlabel('Theta')
plt.ylabel('Intensity')
plt.legend()
plt.grid(True)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()