import os
import shutil

dir_first = 'my_project'
dir_second = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(dir_first):
    for dir_odd in dir_second:
        if not os.path.exists(dir_odd):
            dir_path = os.path.join(dir_first, dir_odd)
            os.makedirs(dir_path)
        else:
            shutil.copytree(dir_odd, os.path.join(dir_first, dir_odd))
            shutil.rmtree(dir_odd)
else:
    print('Каталог my_project уже существует')
