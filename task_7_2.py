import os
import shutil


def parser(text_file, directory_path):

    string = text_file.split('\n')
    for elem in string:
        if elem[0] != '-':
            firs_dir = elem
            dir_path = os.path.join(directory_path, firs_dir)
            os.makedirs(dir_path)
        elif elem[0] == '-' and elem[1] != '-':
            second_dir = elem[1:]
            dir_path = os.path.join(directory_path, firs_dir, second_dir)
            os.makedirs(dir_path)
        elif elem[1] == '-' and elem[2] != '-':
            third_dir = elem[2:]
            if elem[-3] != '.' and elem[-4] != '.':
                dir_path = os.path.join(directory_path, firs_dir, second_dir, third_dir)
                os.makedirs(dir_path)
            else:
                file_name = open(os.path.join(directory_path, firs_dir, second_dir, third_dir), "w+")
                file_name.close()
        elif elem[2] == '-' and elem[3] != '-':
            fourth_dir = elem[3:]
            if elem[-3] != '.' and elem[-4] != '.':
                dir_path = os.path.join(directory_path, firs_dir, second_dir, third_dir, fourth_dir)
                os.makedirs(dir_path)
            else:
                file_name = open(os.path.join(directory_path, firs_dir, second_dir, third_dir, fourth_dir), "w+")
                file_name.close()
        elif elem[3] == '-':
            fifth_dir = elem[4:]
            if elem[-3] != '.' and elem[-5] != '.':
                dir_path = os.path.join(directory_path, firs_dir, second_dir, third_dir, fourth_dir, fifth_dir)
                os.makedirs(dir_path)
            else:
                file_name = open(os.path.join(directory_path, firs_dir, second_dir, third_dir, fourth_dir, fifth_dir),
                                 "w+")
                file_name.close()


working_dir = os.getcwd()
file_yaml = 'config.yaml'
if not os.path.exists('my_project'):
    with open(file_yaml, 'r', encoding='UTF-8') as f:
        parser(f.read().strip(), working_dir)
