def get_grade(marks):
    if  marks >= 80:
        return 'A+'
    elif 70 <= marks < 80:
        return 'A'
    elif 60 <= marks < 70:
        return 'A-'
    elif 50 <= marks < 60:
        return 'B'
    elif 40 <= marks < 50:
        return 'C'
    else:
        return 'F'


for number in range(10,100,10):
    print(f'{number} = {get_grade(number)}')
