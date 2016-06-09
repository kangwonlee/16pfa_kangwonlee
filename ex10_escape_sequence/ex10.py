tabby_cat = "\tI'm tabbed in."
tabby_cat2 = "    I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
# TODO : Escape Sequence
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print("%%s : %s" % tabby_cat)
print("%%r : %r" % tabby_cat)
print("%%s : %s" % tabby_cat2)
print("%%r : %r" % tabby_cat2)
print("%%s : %s" % persian_cat)
print("%%r : %r" % persian_cat)
print("%%s : %s" % backslash_cat)
print("%%r : %r" % backslash_cat)
print(fat_cat)
