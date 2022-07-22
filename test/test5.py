import cv2
import numpy as np
#pip install numpy

# 元画像
img_original = cv2.imread("cry.png")

# 比較対象画像１枚目(同じ画像)
img_comparison1 = cv2.imread("cry.png")

# 比較対象画像２枚目(違う画像)
img_comparison2 = cv2.imread("smile.png")
img_comparison3 = cv2.imread("miko.png")


# 画像が完全一致するかを判定する
#print(np.array_equal(img_original, img_comparison1))
#print(np.array_equal(img_original, img_comparison2))

print(np.count_nonzero(img_original - img_comparison1))
print(np.count_nonzero(img_original - img_comparison2))
print(np.count_nonzero(img_original - img_comparison3))
