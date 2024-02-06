# 나이를 통한 출생년도 알아보기
a = int(input('나이 입력: '))
print( '출생 년도는', 2023-a, '입니다.')


# 정사각형 넓이 계산 프로그램
a = float(input('정사각형 한 변의 길이: '))
print(' 한 변의 길이가', a, 'cm라면', '넓이는', a**2 , '입니다.')


# 1.선생님 풀이
age = int(input('나이가 어떻게 되십니까?'))
print(f"나이가 {age}살 이라면, 출생년도는 {2025 - age}년 입니다.")

# 2.선생님 풀이
side = int(input("한 변의 길이: "))
print(f"한 변의 길이가 {side}cm이면, 넓이는 {side ** 2}cm^2 입니다.")


# 삼각형의 밑변과 높이가 있을 때 넓이 계산
base = float(input("삼각형의 밑변의 길이: "))
height = float(input("삼각형의 높이의 길이: "))
print(f"삼각형의 넓이는 { base * height * 0.5} 입니다.")


# 정수 분리기 프로그램
number = int(input("10000부터 99999사이의 정수: "))
print(f"만의 자리 숫자는 {number//10000}, 천의 자리 숫자는{number // 1000 % 10}, 백의 자리 숫자는 {number//100 % 10}, 십의 자리 숫자는 {number // 10 % 10 }, 일의 자리 숫자는 {number % 10}입니다. ")


# 시간 변환기 프로그램
number = int(input("양의 정수를 입력하세요: "))
print(f"")


# 정수 분리기 프로그램 선생님 풀이
num = int(input("10000~99999 사이 정수 입력: "))
ten_thousands = num // 10000
thousands = (num % 10000) // 1000
hundred = (num % 1000) //100
ten = (num % 100) //10
one = (num % 10)
print(f"{ten_thousands}만 {thousands}천 {hundred}백 {ten}십 {one} 입니다.")


