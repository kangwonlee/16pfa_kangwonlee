# -*- coding: cp949 -*-
# [�й�] [�̸�] [�й�]
# ������: http://learnpythonthehardway.org/book/ex5.html

# ���� �ּ��� �޾� ���ÿ�

my_name = 'Kangwon Lee' # ���� �ڽ��� �̸�
my_age = 25 # a lie
my_height_cm = 180 # also a lie in centimeters
my_weight_kg = 70 # �������� ���� ��� �ٶ�
my_eyes = "Brown" # �������� ��κ� ����
my_teeth = "White"
my_hair = 'Brown'

print "Let's talk about %s." % my_name
# He -> She if appropriate
print "He's %d centimeters tall." % my_height_cm
print "He's %d kilograms heavy." % my_weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % ( my_eyes, my_teeth )
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height_cm, my_weight_kg, my_age + my_height_cm + my_weight_kg)

# ���� ���� �ּ��� �� �� �� diff, commit

# �� �ۿ� �ٸ� study drills �׸�鵵 �õ��� ���鼭 �ʿ�� diff, commit
