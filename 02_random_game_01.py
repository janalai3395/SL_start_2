'''
숫자 추측 게임 만들기

[문제 분석]
사용자가 입력한 값과 컴퓨터가 생성한 랜덤 값을 비교한다.
몇번만에 맞추었는지 알려준다.

사용자에게 힌트를 준다.
사용자가 입력한 값보다 랜덤값 보다 크면 숫자는 작다라고 한다.
사용자가 입력한 값보다 랜덤값 보다 작으면 숫자는 크다라고 한다.

사용자가 입력하여 힌트를 받을떄마다 count 를 증가한다

'''
import random

count=1
Right_answer=random.randrange(1,31) #1~30 중에 한 숫자를 answer 에 저장
print("랜덤게임을 시작합니다. 0을 입력하면 종료합니다.")

while True: #게임 실행부분
    answer=int(input("정답을 입력해주세요:"))
    if answer == 0: #0을 입력받을시
        print("게임을 종료합니다.")
        break
    elif Right_answer == answer : #정답을 입력받았을떄
        print("축하드립니다 정답은 : {} 입니다".format(Right_answer))
        print("{}번만에 정답을 찾으셨습니다.".format(count))
        print("게임을 다시 시작합니다.")
        count=1
        Right_answer=random.randrange(1,31) #1~30 중에 한 숫자를 answer 에 다시 저장
    elif answer < Right_answer : #입력받은 답보다 정답이 클경우
        print("정답은 더 큽니다.")
        count+=1
    else: #Right_answer > answer : #입력받은 답보다 정답이 작을경우
        print("정답은 더 작습니다")
        count+=1
    
