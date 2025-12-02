# This code performs image compression using K-Means clustering.
# It reads an image, reduces its number of colors to 16 by clustering similar pixels.
import cv2, numpy as np
from sklearn.cluster import KMeans
img = cv2.imread("boat.png"); h,w = img.shape[:2]; X = img.reshape(-1,3)
# Apply K-Means clustering with 16 color clusters
k = KMeans(n_clusters=16).fit(X)
# Replace each pixel with the color of its assigned cluster center
out = k.cluster_centers_[k.labels_].astype("uint8").reshape(h,w,3)
cv2.imwrite("compressed.png", out)




