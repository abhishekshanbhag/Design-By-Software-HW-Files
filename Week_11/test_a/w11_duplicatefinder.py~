# AUTHOR Abhishek Shanbhag anshan@bu.edu
# AUTHOR hari chhari@bu.edu
# AUTHOR ameya apastamb ameyama@bu.edu
# AUTHOR Shreyas joshi svmjoshi@bu.edu
from os import listdir
import numpy as np
import hashlib
from skimage.io import imread


def trim_zero_border(arr):
    nzrows = np.nonzero(np.sum(arr, (1, 2)))[0]
    nzcols = np.nonzero(np.sum(arr, (0, 2)))[0]
    return arr[nzrows[0]:nzrows[-1]+1, nzcols[0]:nzcols[-1]+1]


def convert_to_num(arr):
    num = []
    for i in arr:
        for j in i:
            num.append((j[0]*3) + j[1]*2 + j[2])
    return np.resize(num, (arr.shape[0], arr.shape[1]))


def sort_like_images(fl):
    sl = {}
    for i in fl:
        img = convert_to_num(trim_zero_border(255 - imread(fl[i])))
        add_new = True
        for counter in range(4):
            img = np.transpose(img)
            key = hashlib.sha1(img.flatten()).hexdigest()
            if(key in sl):
                sl[key].append(fl[i])
                add_new = False
            img = np.fliplr(img)
            key = hashlib.sha1(img.flatten()).hexdigest()
            if(key in sl):
                sl[key].append(fl[i])
                add_new = False
        if(add_new):
            sl.update({key: [fl[i]]})
    return sl


def sorted_write(sorted_list):
    sld = {}
    for i in sorted_list:
        try:
            slf = sorted_list[i][0]
            m = slf[len(sorted_list[i][0]) - 6: len(sorted_list[i][0]) - 4]
            key = int(m)
        except:
            slf = sorted_list[i][0]
            m = slf[len(sorted_list[i][0]) - 5: len(sorted_list[i][0]) - 4]
            key = int(m)
        sld.update({key: sorted_list[i]})
    with open('answers.txt', "w") as f:
        for lst in sorted(sld):
            f.write(' '.join(sld[lst]) + '\n')
    f.close()


file_list = {}
for i in listdir('.'):
    if i.endswith('png'):
        try:
            key = int(i[len(i) - 6: len(i) - 4])
        except:
            key = int(i[len(i) - 5: len(i) - 4])
        file_list.update({key: i})
sorted_list = sort_like_images(file_list)
sorted_write(sorted_list)
print(hashlib.sha256(open('answers.txt', 'rb').read()).hexdigest())
