import imageio
import imgaug as ia
import imgaug.augmenters as iaa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import os
import cv2
#globbing utility.
import glob

path = "C:\Users\user\face_classification\trainingData"
seq=iaa.Fliplr(p=1.0)
for folder in os.listdir(path):
    i = 0
    for fname in os.listdir(path + '\\' + folder):
        img = imageio.imread(path + '\\' + folder + '\\' + fname)
        print('Original:')
        ia.imshow(img)
        img_aug = seq.augment_image(img)
        print('Augmented:')
        ia.imshow(img_aug)

        imageio.imwrite(os.path.join(path, path + '\\' + folder + '\\' + folder + "%06d.png" % (i,)), img_aug)
        i += 1