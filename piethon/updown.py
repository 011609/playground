# simple up & down game

import random

a = input('TYPE FIRST NUM : ')
b = input('TYPE SECOND NUM : ')

com = random.randint(int(a), int(b))

tries = 1

while True:
    mynum = int(input(f'Guess a number between {a}~{b} : '))

    if com == mynum:
        print('*clapclap*')
        print(f'총 시도 횟수 : {tries}')
        break

    if com > mynum:
        print('up')
        tries = tries + 1

    if com < mynum:
        print("down")
        tries = tries + 1