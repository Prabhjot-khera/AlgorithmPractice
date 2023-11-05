


from statistics import *
def get_grades():                                               #FUNCTION TO GET GRADES FROM USER CODE
    marks_total=[] 
    for students in range(12):                                  #THERE WILL BE 12 ROWS OF MARKS AS THERE ARE 12 STUDENTS
        marks=[] #RESET MARKS LIST FOR EVERY STUDENT
        for mark in range(5): # THERE ARE 5 TEST MARKS PER STUDENT
            marks.append(int(input('enter grade here for student[every 5 grades it goes to next student]: ')))
        marks_total.append(marks) #APPEND STUDENT MARKS TO TOTAL LIST
    return marks_total

grades=get_grades()  #CREATING VARIBLE FOR THE GRADES LIST

def show_grades(grades):
    for student in grades:# DISPLAYING THE GRADES LIST RECEIVED FROM USER INPUT
        print (student)
show_grades(grades)

def studentavg(student):  #STUDENT PARAMETER TO DECIDE WHICH STUDENT TO GET THE AVERAGE OF
    print('the average for this student is:',mean(grades[student])) #RETURNING THE AVERAGE OF THE STUDENT

studentavg(int(input('enter student number(0-11):')))  #CALLING FUNCTION WHILE GETTING PARAMETERS

def testavg(test):
    test_marks=[] #CREATING TO LIST TO HOLD CERTAIN TEST MARKS
    for i in range(len(grades)):  #ITERATING THROUGH EACH ROW
        test_marks.append(grades[i][test])  # APPENDING THE TEST NEEDED FROM EACH TOW
    print('the average for this test is:',mean(test_marks)) #PRINTING THE AVG OF THAT TEST SCORE


testavg(int(input('enter test(0-4):')))
    




