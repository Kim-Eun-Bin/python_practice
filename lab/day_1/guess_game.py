import random

guess_number = random.randint(1, 100)

count = 0
while 1:
    num = int(input('숫자를 입력하세요(1 ~ 100) : '))
    if num == guess_number:
        print(f'정답은 {guess_number}입니다. {count}번만에 성공하셨습니다.')
        break
    elif num > guess_number:
        print('숫자가 너무 큽니다.')
        count += 1
    elif num < guess_number:
        print('숫자가 너무 작습니다.')
        count += 1