# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex40.html

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

import mystuff

mystuff.apple()
print(mystuff.tangerine)


class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


# end class MyStuff

thing = MyStuff()
thing.apple()
print(thing.tangerine)

# 입력 후 add, commit  # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit  # 오류노트 에 각자 오류노트 작성
