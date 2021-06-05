import os

dir_first = 'my_project'
dir_second = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(dir_first):
    for dir_odd in dir_second:
        dir_path = os.path.join(dir_first, dir_odd)
        os.makedirs(dir_path)
else:
    print('Каталог my_project уже существует')
