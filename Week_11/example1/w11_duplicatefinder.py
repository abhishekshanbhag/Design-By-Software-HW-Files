from os import listdir
import numpy as np
import re
import hashlib
from skimage.io import imread
import matplotlib.pyplot as plt


def trim_zero_border(arr):
    nzrows = np.nonzero(np.sum(arr, (1, 2)))[0]
    nzcols = np.nonzero(np.sum(arr, (0, 2)))[0]
    return arr[nzrows[0]:nzrows[-1]+1, nzcols[0]:nzcols[-1]+1]


def sort_files(fl):
    sorted_files_dict = {}
    sf = []
    for item in fl:
        try:
            key = int(item[len(item) - 6: len(item) - 4])
        except:
            key = int(item[len(item) - 5: len(item) - 4])
        sorted_files_dict.update({key: item})
    for i in sorted_files_dict:
        sf.append(sorted_files_dict[i])
    return sf


def convert_to_num(arr):
    num = []
    for i in arr:
        for j in i:
            if(np.array_equal(j, [0, 0, 0])):
                num.append(0)
            elif(np.array_equal(j, [0, 255, 255])):
                num.append(1)
            elif(np.array_equal(j, [255, 0, 255])):
                num.append(2)
            elif(np.array_equal(j, [255, 255, 0])):
                num.append(3)
            elif(np.array_equal(j, [0, 0, 255])):
                num.append(4)
            elif(np.array_equal(j, [255, 0, 0])):
                num.append(5)
            elif(np.array_equal(j, [0, 255, 0])):
                num.append(6)
            else:
                num.append(7)
    return np.resize(num, (arr.shape[0], arr.shape[1]))


def sort_like_images(fl):
    sl = []
    sl.append([fl[0]])
    fl = fl[1:]
    for i in fl:
        create_new = True
        img2 = convert_to_num(trim_zero_border(255 - imread(i)))
        for item in sl:
            img1 = convert_to_num(trim_zero_border(255 - imread(item[0])))
            if(compare(img1, img2)):
                create_new = False
                item.append(i)
        if(create_new):
            sl.append([i])
    return sl


def compare(img1, img2):
    counter = 0
    while(counter < 4):
        img2 = np.transpose(img2)
        if(np.array_equal(img1, img2)):
            return True
        img2 = np.fliplr(img2)
        if(np.array_equal(img1, img2)):
            return True
        counter += 1
    return False


def write_answer_file(sorted_list):
    with open('answers2.txt', "w") as f:
        for lst in sorted_list:
            s = ""
            for item in lst:
                s += item + " "
            s = s[0:len(s)-1]
            s += '\n'
            f.write(s)
    f.close()


def main():
    file_list = []
    for i in listdir('.'):
        if i.endswith('png'):
            file_list.append(i)
    file_list = sort_files(file_list)
    sorted_list = sort_like_images(file_list)
    write_answer_file(sorted_list)


if __name__ == '__main__':
    main()
