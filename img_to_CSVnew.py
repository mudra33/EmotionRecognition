import cv2
import numpy as np
import imageio
import os
import pandas as pd
path = "C:/Users/user/face_classification/src/augmented_training_data"
os.chdir(path)
lists = os.listdir(path)
labels = []
file_lst = []
values = []
for folder in os.listdir(path):
    # files = os.listdir(path + "/" + folder)
    for file in os.listdir(path + "/" + folder):
        path_file = path + "/" + folder + "/" + file
        file_lst.append(path_file)
        labels.append(folder)
        img_file = cv2.imread(os.path.join(path + "/" + folder, file), cv2.IMREAD_GRAYSCALE)
        value = np.asarray(img_file)
        value = value.reshape(-1)
        values.append(value)
dictP_n = {"emotion": labels, "pixels": values,
           "Usage": labels}
data = pd.DataFrame(dictP_n, index=None)
data = data.sample(frac=1)
data['Usage'] = data['emotion'].replace(
    {"0": "Training", "1": "Training", "2": "Training", "3": "Training", "4": "Training", "5": "Training",
     "6": "Training"})
data.to_csv("C:/Users/user/face_classification/file.csv", index=None)