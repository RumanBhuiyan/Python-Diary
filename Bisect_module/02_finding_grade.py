from bisect import bisect, bisect_left
from timeit import default_timer


# noob solution of multiple if-else statement
def get_grade(mark):
    grade = ''
    if mark >= 80:
        grade = 'A+'
    elif mark >= 70:
        grade = 'A'
    elif mark >= 60:
        grade = 'A-'
    elif mark >= 50:
        grade = 'B'
    elif mark >= 40:
        grade = 'C'
    else:
        grade = 'F'
    return grade


# lets see the smallest solution of above if-else statement
def get_grade2(mark):
    grades = ['F', 'C', 'B', 'A-', 'A', 'A+']
    marks = [40, 50, 60, 70, 80]
    index = bisect(marks,mark)
    return grades[index]


def get_grade3(mark):
    grades = ['F', 'C', 'B', 'A-', 'A', 'A+']
    marks = [40, 50, 60, 70, 80]
    index = bisect_left(marks, mark) + 1 if mark in marks else bisect_left(marks, mark)
    return grades[index]


def get_grade4(mark):
    grades = ['A+', 'A', 'A-', 'B', 'C', 'F']
    marks = [mark >= 80, mark >= 70, mark >= 60, mark >= 50, mark >= 40, 1]
    return grades[marks.index(1)]


# call get_grade()
start = default_timer()
for mark in range(10,100,10):
    # print(get_grade(mark))
    pass
end = default_timer()
print(f'get_grade() took {round(end - start,6)} seconds')


# call get_grade2()
start = default_timer()
for mark in range(10,100,10):
    # throw the error message if condtion is false
    assert get_grade(mark) == get_grade2(mark), 'Result didn\'t match'
    # print(get_grade2(mark))
end = default_timer()
print(f'get_grade2() took {round(end - start,6)} seconds')


# call get_grade3()
start = default_timer()
for mark in range(10,100,10):
    # throw the error message if condtion is false
    assert get_grade(mark) == get_grade3(mark), 'Result didn\'t match'
    # print(get_grade3(mark))
end = default_timer()
print(f'get_grade3() took {round(end - start,6)} seconds')

# call get_grade4()
start = default_timer()
for mark in range(10,100,10):
    # throw the error message if condtion is false
    assert get_grade(mark) == get_grade4(mark), 'Result didn\'t match'
    # print(get_grade4(mark))
end = default_timer()
print(f'get_grade4() took {round(end - start,6)} seconds')
