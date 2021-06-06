import os
import sys


def quantification(size_threshold):

    count = 0
    for item in os.scandir(folder):
        if item.stat().st_size < size_threshold:
            count += 1
    return count


folder = sys.argv[1]
if os.path.isdir(folder) is True:
    dict_size_file = {}
    for i in range(10):
        size_file = 10 * 10 ** i
        number_of_files = quantification(size_file)
        dict_size_file.update({size_file: number_of_files})
    print(dict_size_file)
else:
    print('Заданной директории не существует. Проверьте правильно ли указанно имя.')






