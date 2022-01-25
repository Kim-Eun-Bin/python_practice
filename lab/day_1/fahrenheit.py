'''
    섭씨를 화씨로 변환
    화씨온도는 소수점이하 둘째자리까지 출력
'''

print('변환하고 싶은 섭씨 온도를 입력하세요')
temperature = float(input())

fah = ((9 / 5) * temperature) + 32

print('섭씨온도 : ', temperature)
print('화씨온도 : {:.2f}R'.format(fah))
print(f'화씨온도 {fah:.2f}')