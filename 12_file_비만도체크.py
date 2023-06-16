'''
키와 몸무게로 비만도 계산하기


'''
with open("info.txt","r") as file:
    for line in file :      #strip() 공백제거, splite*(","") ,를 구분자로 쓰겠다
        (name, weight, height) = line.strip().split(",")

        if (not name) or (not weight) or (not height):
            continue

    #비만도 계산하기 
    bmi = int(weight) / ((int(height) / 100) ** 2)
    if bmi >= 25 :
        result = '과체중'
    elif bmi >= 18.5 :
        result = "정상 체중"
    else :
        result = "저체중"

    print("\n".join(["이름 : {}",
                    "몸무게 : {}",
                    "키 : {}",
                    "bmi : {:.2f} ",
                    "결과 : {}"])
                    .format(name,weight,height,bmi,result))
    print()