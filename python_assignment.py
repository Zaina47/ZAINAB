'''
yOU WILL EXPLAIN THIS CODE TO ME, LINE BY LINE ON FRIDAY-6/10/23
'''

print('Enter your academic details')
print('\n')
"""An empty dictionary to hold the details of students"""
students_details={}
size=int(input('Enter the size of the dictionary:'))
for i in range(size):
    name = str(input('Enter student name:'))
    reg_no = str('Enter student registration number:')
    age = int(input('Enter student age:'))
    program = str(input('Enter student program:'))
    year_of_study = int(input('Enter student year of study:'))
    subjects = {}
    for i in range(1):
        subject1 = str(input('Enter first subject:'))
        subject2 = str(input('Enter second subject:'))
        subject3 = str(input('Enter third subject:'))
        subjects['subject1'] = subject1
        subjects['subject2'] = subject2
        subjects['subject3'] = subject3
    scores = {}
    for i in range(1):
           marks1 = int(input('Enter marks for subject1:'))
           marks2 = int(input('Enter marks for student2:'))
           marks3 = int(input('Enter marks for student3:'))
           scores['marks1'] = marks1
           scores['marks2'] = marks2
           scores['marks3'] = marks3
    grades = {}
    for i in range(1):
           grade1 = str(input('Enter grades for marks1:'))
           grade2 = str(input('Enter grades for marks2:'))
           grade3 = str(input('Enter grades for marks3:')) 
           grades['grade1'] = grade1
           grades['grade2'] = grade2
           grades['grade3'] = grade3
    students_details['reg_no'] = {
            'Name':name,
            'Age' :age,
            'Program':program,
            'Year of study':year_of_study,
            'Subjects':subjects,
            'Score':scores,
            'Grade':grades}
def find_max_min_marks(values):
    max_mark = max(values)
    min_mark = min(values)
    return max_mark,min_mark
for reg_no,student in students_details.items():
        max_marks,min_marks = find_max_min_marks(student['scores'].values())
print(f"Student:{student['Name']},max marks:{max_marks},min marks:{min_marks}")
    
    
print(students_details)
                   
