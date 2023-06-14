'''
continue 
'''
# 리스트의 값 10 개 중에서 10 보다 큰 수를 출력하시오.
numbers = [12, 27, 93, 48, 61, 71, 24, 54, 72, 78]

print("리스트 값 중 10보다 큰수 - 반복문 사용")

for i in numbers :
    if i >= 10 :
        print(i, end=', ')

print()

print("리스트 값 중 10보다 큰수 - continue 사용")

for i in numbers :
    if i < 10:
        continue
    print(i, end=', ')

print()

#1~30 사이에 수 중에서 7의 배수만 출력하시오. -continue 사용

print("1~30 사이에 수 중에서 7의 배수만 출력하시오. -continue 사용")
for i in range(1,31):
    if i%7 == 0 :
        print(i,end=', ')
    elif i < 30:
        continue


for i in range(1, 31):
    if i % 7 != 0:
        continue
    print(i,end=', ')
print()

