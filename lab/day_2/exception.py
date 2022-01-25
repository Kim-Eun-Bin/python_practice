for i in range(10):
    try:
        result = 10 // i
    except ZeroDivisionError as e:
        print(e)
    else:
        print(result)
    finally:
        print('-------')