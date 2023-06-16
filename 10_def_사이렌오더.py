'''
사이렌 오더를 통해 음료를 미리 예약하는 프로그램을 만드시오.
1.메뉴는 아메리카노 2500원
2.카페라떼 3000원
3.바닐라 라떼 3000원입니다.
메뉴 번호를 선택하면 해당 메뉴와 가격을 출력해 주는 부분을
함수로 작성하시오.

선택한 메뉴는 인수로 전달되어
가격이 결과 값으로 반환(return)되는 함수로 작성하시오.


사용자가 음료를 선택하면 음료의 가격을 알려주는 프로그램
'''
coffee_menu=["아메리카노","카페라떼","바닐라 라떼"]
coffee_price=[2500,3000,3000]
def menu(num):
    if num == 1:
        return coffee_menu[0],coffee_price[0]
    elif num == 2:
        return coffee_menu[1],coffee_price[1]
    elif num == 3:
        return coffee_menu[2],coffee_price[2]
    else :
        print("아닌데?")


while True:
    input_num=int(input("메뉴 번호를 선택해주세요 0번으로 종료"))
    if input_num == 0:
        print("프로그램을 종료합니다.")
        break
    print(menu(input_num))