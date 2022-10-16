print()
grade_percentage = float(input('What is the grade percentage? '))

if grade_percentage >= 90:
    grade_letter = 'A'
elif grade_percentage >= 80:
    grade_letter = 'B'
elif grade_percentage >= 70:
    grade_letter = 'C'
elif grade_percentage >= 60:
    grade_letter = 'D'
elif grade_percentage < 60:
    grade_letter = 'F'

if grade_percentage % 10 >= 7:
    grade_sign = '+'
    if grade_letter == 'A' \
    or grade_letter == 'F':
        grade_sign = ''
elif grade_percentage % 10 <= 3:
    grade_sign = '-'
    if grade_letter == 'F':
        grade_sign = ''
else:
    grade_sign = ''


if grade_percentage >= 70:
    print(f'Congratulations! Your grade is {grade_letter}{grade_sign}.')
else:
    print(f'Your grade is {grade_letter}{grade_sign}. You can do better next time.')