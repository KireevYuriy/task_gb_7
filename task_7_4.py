import os
import sys
import random


def quantification(size_threshold, folders):

    count = 0
    for item in os.scandir(folders):
        if item.stat().st_size < size_threshold:
            count += 1
    return count


folder_dir = 'some_data'
if not os.path.isdir(folder_dir):
    os.mkdir(folder_dir)
    letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    for _ in range(10 ** 2):
        f_name = ''.join(random.sample(letters, random.randint(5, 10)))
        f_exp = ''.join(random.sample(letters, random.randint(2, 3)))
        f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5)))
        with open(os.path.join(folder_dir, f'{f_name}.{f_exp}'), 'wb') as f:
            f.write(f_content)

folder = sys.argv[1]
if os.path.isdir(folder) is True:
    dict_size_file = {}
    for i in range(5):
        size_file = 10 * 10 ** i
        number_of_files = quantification(size_file, folder)
        dict_size_file.update({size_file: number_of_files})
    print(dict_size_file)
else:
    print('Заданной директории не существует. Проверьте правильно ли указанно имя.')

