# -*- coding: cp949 -*-
import re

f = open("repo_list.txt", 'r')
txt = f.read()
f.close()

# regular expression �� �̿��Ͽ� ���� ���ڿ��� ã��
found = re.findall("https://.+[/,](.+).git", txt)
print "len(found) =", len(found)
while found:
    item = found.pop()
    print item, 
    print "\t[ duplicate =", item in found, ']'
