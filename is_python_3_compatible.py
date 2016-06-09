import os


def main():
    dir_list = os.listdir(os.curdir)
    for name in dir_list:
        if os.path.isdir(name) and 'ex' == name[:2]:
            print(name)


if __name__ == '__main__':
    main()
