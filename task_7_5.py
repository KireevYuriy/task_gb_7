import os
import sys
import random


def quantification(size_threshold, folders):

    list_ext = []
    count = 0
    for item in os.scandir(folders):
        if item.stat().st_size < size_threshold:
            file_ext = os.path.splitext(item)
            list_ext.append(file_ext[1])
            count += 1
    return list_ext, count


folder = sys.argv[1]
if os.path.isdir(folder) is True:
    dict_size_file = {}
    for i in range(5):
        size_file = 10 * 10 ** i
        list_of_files, chek = quantification(size_file, folder)
        dict_size_file.update({size_file: (chek, list_of_files)})
    print(dict_size_file)
else:
    print('Заданной директории не существует. Проверьте правильно ли указанно имя.')
