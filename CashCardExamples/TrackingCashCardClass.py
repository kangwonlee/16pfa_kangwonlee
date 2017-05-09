# -*- coding: utf8 -*-
from SafeCashCardClass import SafeCashCard
# 입출금 시간을 기록하기 위해 time 모듈을 도입
import time


# SafeCashCard 클래스를 상속하여 HistoryCashCard 클래스를 만든다
class HistoryCashCard(SafeCashCard):
    """
    Cash card capable of recording histories
    """  # <- docstring

    def __init__(self):
        print("HistoryCashCard __init__()")
        # HistoryCashCard 클래스의 객체는 사용 내역을 담을
        # 별도의 멤버 변수가 필요함. 이 변수를 준비하려면
        # HistoryCashCard 클래스의 생성자가 필요함

        # 상위 클래스인 SafeCashCard 의 생성자를 먼저 호출
        SafeCashCard.__init__(self)
        # super(HistoryCashCard,self).__init__() 도 가능할 수 있음

        # 입출금 내역을 기록하기 위한 리스트를 준비함
        self.history = []

    # 입출금 기록 기능을 추가하기 위해 입금, 출금 메소드 재정의
    def deposit(self, amount_won):
        """
        HistoryCashCard deposit method
        deposit amount & add record to history
        """  # <- docstring
        print("HistoryCashCard deposit()")
        # 입금 기능 자체는 상위 클래스에 이미 정해진 바를 따른다
        SafeCashCard.deposit(self, amount_won)
        # 또는
        # super(HistoryCashCard,self).deposit(amount_won)

        # 입금 내역 기록
        self.record_history('deposit', amount_won)

    # 출금 내역을 기록하는 출금 메소드
    def withdraw(self, amount_won):
        """
        HistoryCashCard withdraw method
        withdraw amount & add record to history
        """  # <- docstring
        print("HistoryCashCard withdraw()")
        # 출금 기능 자체는 역시 상위 클래스를 따름
        SafeCashCard.withdraw(self, amount_won)

        # 출금 내역 기록
        self.record_history('withdraw', amount_won)

    def record_history(self, activity, amount_won):
        record = {
            'time': time.localtime(),
            'balance': self.check_balance(),
            'activity': activity,
            'amount': amount_won,
        }
        self.history.append(record)

    def show_history(self):
        """
        HistoryCashCard show_history method
        show appended history
        """  # <- docstring
        print("HistoryCashCard show_history()")  # 함수 호출 표식

        # 지금 까지 멤버 변수 self.history에 모인
        # 사용 내역을 하나씩 출력함

        print('%25s %10s %10s %10s' % (
            'time and date', 'activity', 'amount', 'balance'))
        # 사용 내역 루프 시작
        for record in self.history:
            # 각 내역 별로
            # 시간, 잔고 출력
            print('%25s %10s %10d %10d' %
                  (time.asctime(record['time']),
                   record['activity'], record['amount'], record['balance']))
        # 사용 내역 루프 끝


if "__main__" == __name__:
    print("main 객체 생성 ".ljust(60, '*'))
    myHistCard = HistoryCashCard()
    print("main 10000원 입금 ".ljust(60, '*'))
    myHistCard.deposit(10000)
    print("main 9000원 출금 ".ljust(60, '*'))
    myHistCard.withdraw(9000)
    print("main 9000원 출금 ".ljust(60, '*'))
    myHistCard.withdraw(9000)  # 오류가 발생할 것임
    print("main 내역 확인 ".ljust(60, '*'))
    myHistCard.show_history()
    print("main 끝 ".ljust(60, '*'))
