import os
import subprocess


def process_folder(folder_name):
    # store current folder to return
    current_folder = os.path.abspath(os.curdir)

    # change to the given folder
    os.chdir(folder_name)

    dir_list = os.listdir(os.curdir)
    for name in dir_list:
        if os.path.isfile(name) and '.py' == os.path.splitext(name)[-1]:
            print(name)

    # return to stored folder
    os.chdir(current_folder)


def main():
    dir_list = os.listdir(os.curdir)
    for name in dir_list:
        if os.path.isdir(name) and 'ex' == name[:2]:
            print(name)
            process_folder(name)

if __name__ == '__main__':
    main()
