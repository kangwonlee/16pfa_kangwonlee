# -*- coding: cp949 -*-
import re
# regular expression

f = open("140318pfa.txt", 'r')
txt = f.read()
f.close()

# done reading file

# '@dev.naver.com/' �� ���� ���ڿ��� �����ϰ� �յڷ� �ٸ� ���ڰ� �ִ� ��� ����
# txt ���� ã��
found = re.findall(".+@dev.naver.com/.+", txt)

for item in found:
    print item
