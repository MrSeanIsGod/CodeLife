import matplotlib.pyplot as plt
from matplotlib.image import imread
from sklearn.cluster import KMeans
import numpy as np

def compress_image(n_clusters, img_path):
    img = imread(img_path)
    img_size = img.shape
    X = img.reshape(img_size[0] * img_size[1], img_size[2])
    
    km = KMeans(n_clusters=n_clusters)
    km.fit(X)
    X_compressed = km.cluster_centers_[km.labels_]
    X_compressed = np.clip(X_compressed.astype('uint8'), 0, 255)
    X_compressed = X_compressed.reshape(img_size[0], img_size[1], img_size[2])
    
    return X_compressed

# 調用函式進行圖像壓縮
compressed_64 = compress_image(64, 'pokemon.JPG')
compressed_32 = compress_image(32, 'pokemon.JPG')
compressed_16 = compress_image(16, 'pokemon.JPG')

# 顯示壓縮後的圖像
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# 原始圖像
ax[0, 0].imshow(imread('pokemon.JPG'))
ax[0, 0].set_title('Original Image')
ax[0, 0].axis('off')

# 64色壓縮圖像
ax[0, 1].imshow(compressed_64)
ax[0, 1].set_title('Compressed Image with 64 colors')
ax[0, 1].axis('off')

# 32色壓縮圖像
ax[1, 0].imshow(compressed_32)
ax[1, 0].set_title('Compressed Image with 32 colors')
ax[1, 0].axis('off')

# 16色壓縮圖像
ax[1, 1].imshow(compressed_16)
ax[1, 1].set_title('Compressed Image with 16 colors')
ax[1, 1].axis('off')

plt.tight_layout()
plt.show()
