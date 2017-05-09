# -*- coding:utf-8 -*-
import os
import subprocess
from is_python_3_compatible import python3


def process_py_file(filename):
    try:
        f = open(filename, 'r', encoding="utf-8")
        txt = f.read()
        f.close()
    except UnicodeDecodeError:
        f = open(filename, 'r', encoding="cp949")
        txt = f.read()
        f.close()
    except TypeError as e:
        # 'encoding' is an invalid keyword argument for this function
        f = open(filename, 'r')
        txt = f.read()
        f.close()

    patterns = {'argv': 'import argv', 'input': 'raw_input'}

    result = "'%s': {" % filename

    b_OR = False
    for key, signature in patterns.items():
        if signature in txt:
            b_OR = True
            # print("%s needs %s" % (filename, key))
            result += "'%s':[]," % key

    if b_OR:
        result += '},'
        print(result)




def process_folder(folder_name):
    # store current folder to return
    current_folder = os.path.abspath(os.curdir)

    # change to the given folder
    os.chdir(folder_name)

    dir_list = os.listdir(os.curdir)
    for name in dir_list:
        if os.path.isfile(name) and '.py' == os.path.splitext(name)[-1]:
            # print('file %s' % name)
            process_py_file(name)

    # return to stored folder
    os.chdir(current_folder)


def main():
    dir_list = os.listdir(os.curdir)
    for name in dir_list:
        if os.path.isdir(name) and 'ex' == name[:2]:
            # print('folder %s' % name)
            process_folder(name)


if __name__ == '__main__':
    main()
