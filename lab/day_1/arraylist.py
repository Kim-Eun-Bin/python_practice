kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

sum = 0
for j in range(len(midterm_score[0])):
    for i in range(len(midterm_score)):
        sum += midterm_score[i][j]
    average = sum / len(midterm_score)
    print(f'average = {average:.2f}')
    sum = 0