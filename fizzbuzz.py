import sys

numbers = [int(i) for i in sys.argv[1:]]

for i in numbers:
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)
