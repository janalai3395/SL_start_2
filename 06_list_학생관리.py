'''
"학생 관리" 프로그램을 작성하시오.
이 프로그램은 종료 시킬 떄까지 무한 반복된다.
- "작업 선택 : "에서 0 입력 시 프로그램이 종료된다.
- "작업 선택 : "에서 1 입력 시 관리하는 학생 목록이 조회된다.
- "작업 선택 : "에서 2 입력 시 학생을 추가할 수 있다.
- "작업 선택 : "에서 3 입력 시 학생을 삭제할 수 있다.
이떄 입력한 학생은 관리하는 학생 목록에 있는 데이터만 삭제 가능하도록 하며 목록에 없는 학생을 삭제하고자 할 떄는
'삭제할 학생이 없습니다. 다시 입력하세요!'를 화면에 출력한다
'''
def compare_list(name,comparelist):
    for element in comparelist:
        if element == name:
            return True
    return False

student_list=[]

print("학생 관리 프로그램입니다.")
while True :
    print("0 입력 시 프로그램이 종료됩니다.")
    print("1 입력 시 관리하는 학생 목록이 조회됩니다.")
    print("2 입력 시 학생을 추가할 수 있습니다.")
    print("3 입력 시 학생을 삭제할 수 있습니다.")

    temp_main = int(input("번호를 입력해주세요:"))

    if temp_main == 0 :
        print("프로그램을 종료합니다.")
        break
    elif temp_main == 1 :
        print("학생 목록을 출력합니다.")
        print(student_list)
    elif temp_main == 2 :
        insert_student_name=input("추가할 학생 이름을 입력해주세요 :")
        student_list.append(insert_student_name)
    elif temp_main == 3 :
        remove_student_name=input("삭제할 학생 이름을 입력해주세요:")
        temp_compare=compare_list(remove_student_name,student_list)
        if temp_compare == 1:
            student_list.remove(remove_student_name)
            print("삭제되었습니다.")
        elif temp_compare == 0:
            print("일치하는 학생이 없습니다.")
            continue
    else:
        print("다시 입력해주세요")
