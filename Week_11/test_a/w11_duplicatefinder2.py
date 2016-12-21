# AUTHOR Vrushali Mahajan vmahajan@bu.edu
from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib

directory = "."


def files_index(filename):
    return int(re.split(r'\d+', filename)[0])


def get_key(file1):
    return int(re.findall(r'\d+', file1[0])[0])


def crop(image):
    rows = np.nonzero(np.sum(image, (1, 2)))[0]
    columns = np.nonzero(np.sum(image, (0, 2)))[0]
    return image[rows[0]:rows[-1] + 1, columns[0]:columns[-1]+1]


images = dict()
for file in listdir(directory):
    if file.endswith(".png"):
        image = crop(255 - imread(directory+"/"+file))
        flag = False
        for i in range(0, 4):
            hex1 = (hashlib.sha1(np.rot90(image, i).flatten()).hexdigest())
            hex2 = (hashlib.sha1(
                np.fliplr(np.rot90(image, i)).flatten()).hexdigest())
            if hex1 in images:
                flag = True
                images[hex1].append(file)
                break
            elif hex2 in images:
                flag = True
                images[hex2].append(file)
                break
        if not flag:
            images[hex1] = list([file])

for key in images:
    images[key].sort(key=files_index)

with open("answers.txt", 'w') as file:
    for line in sorted(images.values(), key=get_key):
        file.write(' '.join(line) + '\n')

print(hashlib.sha256(open('answers.txt', 'rb').read()).hexdigest())
