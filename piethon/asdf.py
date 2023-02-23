import pygame # 모듈을 불러옵니다.

pygame.init() # 항상 코드 맨 위에 있어야 합니다.

# 변수
hw = (960, 640) # 창크기 변수입니다.
screen = pygame.display.set_mode(hw) # 스크린 변수입니다. 창크기를 설정합니다.
runing = True # 플래이중인지를 나타냅니다.

# 세팅
pygame.display.set_caption("테트리스") # 창의 이름을 정합니다.

while runing:
    for event in pygame.event.get():  # 키입력 감지
        if event.type == pygame.QUIT:  # 나가기 버튼 눌럿을때
            runing = False # 와일문 나가기
pygame.quit() # 게임을 종료합니다