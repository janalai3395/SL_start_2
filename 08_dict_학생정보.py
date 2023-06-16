'''
학생정보를 입력받아서 사전에 저장하고 
검색을 통해서 학번을 입력받으면 이름을 찾아주는 코드
검색값이 공란일시 프로그램을 종료하는 코드

학생정보는 z 를 누르면 종료
학번에서는 빈칸이면 검색 종료

'''

student = {}

while True: #입력부
    idNum=input("학번 입력 : ") #20295001 가나다
    if idNum.lower() == 'z': #z를 누르면 종료
        break
    name=input("이름 입력 : ")
    student[idNum] = name #key <= 값
print("입력 종료")

while True:
    idnum = input("검색하고자 하는 학생의 학번을 입력하세요 : ")
    if idnum == "":
        break
    if idnum in student :
        print("검색결과")
        print("학번 : {} 이름 : {}".format(idnum,student[idNum]))
    else :
        print("다시 입력해주세요")
print("프로그램 종료")
