# simple up & down game

import random

a = input('TYPE FIRST NUM : ')
b = input('TYPE SECOND NUM : ')

com = random.randint(int(a), int(b))

while True:
    mynum = int(input(f'Guess a number between {a}~{b} : '))

    if com == mynum:
        print('*clapclap*')
        break

    if com > mynum:
        print('up')

    if com < mynum:
        print("down")