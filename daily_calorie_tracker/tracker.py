'''
Name:Satyarata Behera
Date:29-09-2025
Project Title:Daily Calorie Tracker
'''
print("Welcome! This tool helps track daily calorie intake.\nGenerates your Total and Average daily calorie intake.\nAlso warns if calorie intake is exceeded.\nThank You!")
start=input('Would You Like to Start(yes/no):')
if start=='yes' or start=='YES' or start=='Yes':
    Calories=[]
    Meals=[]
    n=int(input('Enter Number of Meals Consumed:'))
    for i in range(n):
        a=input('Enter Name of Meal:')
        Meals.append(a)
        intake=int(input('Enter Calories Consumed In Meal:'))
        Calories.append(intake)
    Limit=int(input('Enter daily Calorie Limit:')) 
    print('Meal Name\t\tCalories')
    print('-----------------------')
    for j in range(n):
        M=Meals[j]
        C=Calories[j]
        print(f'{M}\t\t{C}\n\n')
    S=sum(Calories)
    L=len(Calories)
    print(f'total\t\t{S}\n\n')
    print(f'Average\t\t{S/L}\n\n')
    if sum(Calories)>Limit:
        print('WARNING:Daily Intake More Than Limit')
        LimitStatus='Exceeding Limit'#used later in file writing 
    else:
        print('Daily Intake within Limit')
        LimitStatus='Within Limit'#used later in file writing
    Bonus=input('Do You Want A File To Save Report?(yes or no):')
    if Bonus=='Yes' or Bonus=='yes' or Bonus=='YES':
        f=open('Calorie_log.txt','a')#append ('a') is used so that old entries are not truncated.
        time=input('Enter Time of Entry:')
        Entry=str([time,S,S/L,LimitStatus])
        f.writelines(Entry)
        print('File Written')
        f.close()
else:
    print('Code Terminated')
