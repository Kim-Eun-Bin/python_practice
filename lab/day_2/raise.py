while True:
    print('변환할 정수 값을 입력해 주세요 : ')
    value = input()
    for digit in value:
        if digit not in "0123456789":
            raise ValueError('숫자값을 입력하지 않으셨습니다.')
        print('정수로 변환된 숫자 : ', int(value))