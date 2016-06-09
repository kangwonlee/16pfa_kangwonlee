# coding: utf8
import os
import subprocess


def python3():
    from sys import argv
    arg0 = argv[1]

    return arg0


'''
ex11.py needs input
ex12.py needs input
ex13.py needs argv
ex14.py needs argv
ex14.py needs input
ex15.py needs argv
ex15.py needs input
ex16.py needs argv
ex16.py needs input
ex17.py needs argv
ex20.py needs argv
ex31.py needs input
ex35.py needs input
ex41.py needs input
'''


def process_py_file(filename):
    try:
        subprocess.call('%s %s' % (python3(), filename), shell=True)
    except:
        print("%s failed" % filename)
    else:
        print("success %s" % filename)


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
