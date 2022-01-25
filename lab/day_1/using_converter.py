# module import

# module import alias

# method import

# all method import
from lab.day_1.fah_converter import *

print('변환하고 싶은 섭씨온도를 입력하세요.')
temperature = float(input())

result = conver_c_to_f(temperature)

print('섭씨온도 = ', temperature)
print(f'화씨온도 = {result:.2f}')

print(say_hello("python"))