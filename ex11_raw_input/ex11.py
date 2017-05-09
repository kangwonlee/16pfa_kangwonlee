print("How old are you?", ends=' ')
age = input()
print("How tall are you?", ends=' ')
height = input()
print("How much do you weigh?", ends=' ')
weight = input()

print("So you're %r old, %r tall and %r heavy." % (
    age, height, weight
))
