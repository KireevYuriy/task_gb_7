import os
import shutil


if not os.path.isdir('my_project'):
    os.mkdir('my_project')
if not os.path.exists('my_project/templates'):
    os.mkdir('my_project/templates')
first_path = 'my_project/templates'
for dirpath, dirnames, filenames in os.walk('my_project'):
    for dirname in dirnames:
        temp = os.path.join(dirpath, dirname)
        list_str = temp.split('\\')
        if dirname == 'templates' and len(list_str) > 2:
            list_one = os.listdir(os.path.join(dirpath, dirname))
            for elem in list_one:
                if not os.path.exists(os.path.join(first_path, elem)):
                    shutil.copytree(os.path.join(dirpath, dirname, elem), os.path.join(first_path, elem))
