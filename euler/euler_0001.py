# -*-coding:utf8
# http://euler.synap.co.kr/prob_detail.php?id=1
"""
10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.

1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?
"""

result = 0

for i in range(1, 1000):
    if ((i % 3) == 0) or ((i % 5) == 0):
        result += i

print ("result = %d" % result)

# 프로그램 작성 후 add, commit

# 각 행 주석 입력 후 commit
