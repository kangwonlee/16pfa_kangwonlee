# coding: utf8
import os
import subprocess


def python3():
    from sys import argv
    arg0 = argv[1]

    return arg0


need_input = {'ex11.py': {'input': []},
              'ex11_python3.py': {'input': []},
              'ex12.py': {'input': []},
              'ex13.py': {'argv': []},
              'ex14.py': {'argv': [], 'input': []},
              'ex15.py': {'argv': [], 'input': []},
              'ex16.py': {'argv': [], 'input': []},
              'ex17.py': {'argv': []},
              'ex20.py': {'argv': []},
              'ex31.py': {'input': []},
              'ex35.py': {'input': []},
              'ex41.py': {'input': []},
              }


def process_py_file(filename):
    if filename in need_input:
        print("*** %s needs %s" % (filename, need_input[filename].keys()))
    else:
        try:
            subprocess.call('%s %s' % (python3(), filename), shell=True)
        except:
            print("%s failed" % filename)


def process_folder(folder_name):
    # store current folder to return
    current_folder = os.path.abspath(os.curdir)

    # change to the given folder
    os.chdir(folder_name)

    dir_list = os.listdir(os.curdir)
    for name in dir_list:
        if os.path.isfile(name) and '.py' == os.path.splitext(name)[-1]:
            print('file %s' % name)
            process_py_file(name)

    # return to stored folder
    os.chdir(current_folder)


def main():
    dir_list = os.listdir(os.curdir)
    for name in dir_list:
        if os.path.isdir(name) and 'ex' == name[:2]:
            print('folder %s' % name)
            process_folder(name)

if __name__ == '__main__':
    main()
