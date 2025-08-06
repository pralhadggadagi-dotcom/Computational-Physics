import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
dataset="/home/student/Downloads/PetImages"
categories=["Cat","Dog"]
for i in categories:
    path = os.path,join(dataset,i)
    for image in os.listdir(path):
        imagelist = cv2.imread(os.path.join(path,image),cv2.IMREAD_GRAYSCALE)
        plt.imshow(imagelist,cmap="grey")
        plt.show
        break
    break

