from lab.day_1 import date as dt

print(dt.now())
print(dt.today())
current_year = dt.today().year

print(f'현재년도 : {current_year}')
input_year = int(input('태어난 년도를 입력하세요 : '))
print(type(input_year), input_year)

age = current_year - input_year + 1
print(f'나이 : {age}')

if 17 <= age < 20:
    print('고등학생 입니다.')
elif 20 <= age <= 27:
    print('대학생 입니다.')
else:
    print('학생이 아닙니다.')