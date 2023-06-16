'''
사용자로부터 정수를 입력 받아 1부터 입력받은수 까지
369 게임을 진행합니다.
3,6,9 에서는 '짝' 을
10,20,30,..... 배수 자리에는 '만세'를 출력하는 부분은 함수로 작성하시오.
'''

def multiplication_game(num): #함수
    result=[]
    for i in range(1,num+1):
        j= i % 10 
        if j in [3,6,9]:
            result.append("짝")
        elif j == 0:
            result.append("만세")
        else:
            result.append(i)
    return result
#실행부
num=int(input("정수 입력 :"))
print(multiplication_game(num))
