# import random

# rps = ('가위', '바위', '보')

# user = input('"가위", "바위", "보" 중에서 하나를 입력해주쇼 : ')

# com = random.choice(rps)

# if not user in rps:
#     print('"가위", "바위", "보" 중에서 입력하세요;')

# elif user == com:
#     print(f'컴퓨터({com})) VS 유저({user})\n비겼습니다!')

# elif user == '가위' and com == '바위':
#     print(f'컴퓨터({com}) VS 유저({user})\n졌습니다!')

# elif user == '바위' and com == '보자기':
#     print(f'컴퓨터({com}) VS 유저({user})\n졌습니다!')

# elif user == '보자기' and com == '가위':
#     print(f'컴퓨터({com}) VS 유저({user})\n졌습니다!')

# else:
#     print(f'컴퓨터({com}) VS 유저({user})\n이겼슴다!')


####################################################################################


import random

rps = ('가위', '바위', '보')



match = int(input('몇판을 돌린실꺼가요? : '))
WhatRPS = input('무엇으르무 선택하시게스무니까? : ')


# match = int(input('몇판을 돌린실꺼가요? : '))
# WhatRPS = input('무엇으르무 선택하시게스무니까? : ')

tie = 0; win = 0; lose = 0

for x in range(match):

    # WhatRPS = random.choice(rps)

    com = random.choice(rps)

    if com == WhatRPS:
        tie = tie + 1
        print(f'{x + 1}번쨰 판\n결과 : TIE')

    elif WhatRPS == '가위' and com == '바위':
        lose = lose + 1
        print(f'{x + 1}번쨰 판\n결과 : LOSE')

    elif WhatRPS == '바위' and com == '보':
        lose = lose + 1
        print(f'{x + 1}번쨰 판\n결과 : LOSE')

    elif WhatRPS == '보' and com == '가위':
        lose = lose + 1
        print(f'{x + 1}번쨰 판\n결과 : LOSE')

    else:
        win = win + 1
        print(f'{x + 1}번쨰 판\n결과 : WIN')
        
print('')

print('-' * 50)

print(f'\n\n기록 조회 :\n\n이긴 횟수 : {win} \n진 횟수 : {lose} \n비긴 횟수 : {tie}')

print('사실 쪽가위 내면 됨\n\n')

print('-' * 50)

# https://go.microsoft.com/fwlink/?linkid=2168605