import statistics as stat
#Task-1
'''
Name:Satyarata Behera
Date:29-09-2025
Project Title:Daily Calorie Tracker
'''
print("Welcome!\n")
#Task-2
def Data_Input():
    marks_dict={}
    n=int(input("Enter no of students:"))
    for i in range(n):
        Name=input("Enter Student Name:")
        Marks=int(input("Enter Student Marks:"))
        marks_dict[Name]=Marks
    return marks_dict

#Task-3
def calculate_average(marks_dict):
    Avg=stat.mean(marks_dict.values())
    print("Average marks of class is:",Avg)
def calculate_median(marks_dict):
    median=stat.median(marks_dict.values())
    print("Median marks of class is:",median)
def max_score(marks_dict):
    max_mark=max(marks_dict.values())
    print("Max score obtained:",max_mark)
def min_score(marks_dict):
    min_mark=min(marks_dict.values())
    print("Min score obtained:",min_mark)
#Task-4
def Assign_Grade(marks_dict):
    grades_dict={}
    for name,marks in marks_dict.items():
        if marks>=90:
            grade="A"
        elif marks>=80:
            grade="B"
        elif marks>=70:
            grade="C"            
        elif marks>=60:
            grade="D"
        else:
            grade="F"
        grades_dict[name]=grade
    return grades_dict
def Grade_Count(grades_dict):    
    GC={"A":0,"B":0,"C":0,"D":0,"F":0}
    for g in grades_dict.values():
        if g=="A" or g=="B" or g=="C" or g=="D" or g=="F":
            GC[g]+=1
    print(GC)
            

#Task-5
def Pass_Fail(marks_dict):
    passed_students = [name for name, m in marks.items() if m >= 40]
    failed_students = [name for name, m in marks.items() if m < 40]
    print("passed students:",passed_students)
    print("Number of passed students:",len(passed_students))
    print("failed student:",failed_students)
    print("Number of failed students:",len(failed_students))

#Task-6
def Table(marks_dict,grades_dict):
    print("\nName\t\tMarks\tGrade")
    print("---------------------------------")
    for name, mark in marks_dict.items():
        print(f"{name:<12}\t{mark:<6.1f}\t{grades[name]}")

marks={}
grades={}
while True:
    print("\tMenu\n")
    print("1. Enter Marks Data\n2. Find Average marks\n3. Find median marks\n4. Find Max and Min score\n5. Generate grade summary\n6. Pass and Fail Lists\n7. Grade Table Output\n8. Exit Loop")
    choice=int(input("Enter Choice:"))
    if choice==1:
        marks=Data_Input()
        print(marks)
        print("Data Enter Successfully.")
    elif choice==2:
        if marks!={}:
            calculate_average(marks)
        else:
            print("No entries available.")
    elif choice==3:
        if marks!={}:
            calculate_median(marks)
        else:
            print("No entries available.")
    elif choice==4:
        if marks!={}:
            max_score(marks)
            min_score(marks)
        else:
            print("No entries available.")
    elif choice==5:
        if marks!={}:
            grades=Assign_Grade(marks)
            print(grades)
            print("Grade summary generated, perform action 7 for table output.")
            Grade_Count(grades)
        else:
            print("No entries available.")
    elif choice==6:
        if marks!={}:
            Pass_Fail(marks)
        else:
            print("No entries available.")
    elif choice==7:
        if marks!={} and grades!={}:
            Table(marks,grades)
        else:
            print("No entries available.")
    elif choice==8:
        print("Code Terminated")
        break
    
        






















        
        
