def average_valid_numbers():
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    valid_numbers=[item for item in numbers if 0<item<100 ]
    total=0
    for number in valid_numbers:
        total+=number
    average=total/(len(valid_numbers))
    print(format(average,".2f"))

def lottery_generator():
    import random as rd
    DIGIT_OF_LOTTERY_NUMBER=7
    lottery_number=[]
    for digit in range(DIGIT_OF_LOTTERY_NUMBER):
        lottery_number.append(rd.randint(0,9))
    def diplay_lottery_number(lottery_number):
        print("Winner number is : ",end="")
        for digit in lottery_number:
            print(digit,end="")
    diplay_lottery_number(lottery_number)

def rainfall_statistics():
    MONT_OF_YEAR=12
    rain_per_month=[]
    total=0
    for month in range(MONT_OF_YEAR):
        rain_per_month.append(float(input(f"Enter the month {month+1} rain amount: ")))
        total+=rain_per_month[month]
    average=total/MONT_OF_YEAR
    print(f"The total rainfall for the year: {total:,.2f}")
    print(f"The average monthly rainfall: {average:,.2f}")
    print("The months with the highest and lowest amounts: ")
    print(f"Highest:  month:{rain_per_month.index(max(rain_per_month))+1} , amount:{max(rain_per_month):,.2f}")
    print(f"Lowest:  month:{rain_per_month.index(min(rain_per_month))+1} , amount:{min(rain_per_month):,.2f}")

def number_analysis():
    print("Enter a series of 20 numbers: ",end="")
    while True:
        series=input()
        full_of_numbers=True
        if len(series)==20:
            for element in series:
                if element not in ["0","1","2","3","4","5","6","7","8","9"]:
                    full_of_numbers=False
            if full_of_numbers:
                break
            else:
                print("Enter a series of 20 numbers: ",end="")
        else:
            print("Enter a series of 20 numbers: ",end="")  
    series_list=[]
    index=0
    total=0
    for number in series:
        series_list.append(int(number))
        total+=int(series_list[index])
        index+=1
    average=format(total/index,",.2f")
    print(f"The lowest number in the list: {min(series_list)}")
    print(f"The highest number in the list: {max(series_list)}")
    print(f"The total of the numbers in the list: {total}")
    print(f"The average of the numbers in the list: {average}")

def charge_account_validation():
    import a3 
    charge_file=open("charge_accounts.txt","r")
    charge_list=a3.file_to_list("charge_accounts.txt")
    charge_file.close()
    print(charge_list)

def copy():
    charge_file=open("charge_accounts.txt","r")
    charge_list=charge_file.readlines()
    for index in range(len(charge_list)):
        charge_list[index]=charge_list[index].rstrip("\n")
    charge_file.close()
    return charge_list
    
def charge_account_validation_final():    
    try:
        charge_list=copy()
        account_number=int(input("Enter your account number: "))
        charge_list.index(account_number)
    except ValueError:
        print("Invalid number.")

def dice_rolling():
    import random as rd
    while True:
        print("Enter the number of throws: ",end="")
        try:
            number_of_throws=int(input())
            if number_of_throws>0:
                if 7>number_of_throws>0:
                    break
                else:
                    print("Enter a throw number 1-6 : ",end="")
            else:
                print("Throw number cannot be negative or zero: ",end="")                
        except ValueError:
            print("Invalid number.",end="")    
    def rows(number_of_throws):
        throws_list=[]
        for throw in range(number_of_throws):
            throws_list.append(rd.randint(1,10))
        print("Here is the list of results:",end=" ")
        print(sorted(throws_list))
    rows(number_of_throws)

def drivers_licanse_exam():
    import random as rd
    import a3
    NUM_OF_STUDENT=3
    QUESTION_NUMBERS=20
    answer_list=["A","B","C","D"]
    passed_student_number=0
    
    correct_answers_list=a3.file_to_list("correct_answers.txt")
    
    for student in range(NUM_OF_STUDENT):
        answers_file=open(f"student{student+1}.txt","w")
        for i in range(QUESTION_NUMBERS):
            answers_file.write(rd.choice(answer_list)+"\n")
        answers_file.close()
    
    for student in range(NUM_OF_STUDENT):
        answers_file=open(f"student{student+1}.txt","r")
        students_answer_list=answers_file.readlines()
        answers_file.close()
        for index in range(QUESTION_NUMBERS):
            students_answer_list[index]=students_answer_list[index].rstrip("\n")
        correct_questions=0
        incoorect_question_list=[]
        for index in range(QUESTION_NUMBERS):
            if students_answer_list[index]==correct_answers_list[index]:
                correct_questions+=1
            else:
                incoorect_question_list.append(index+1)
        if correct_questions>=15:
            print(f"Student {student+1} was passed the exam.")
            print(f"Correct question numbers: {correct_questions}")
            print(f"Incorrect questions numbers: {QUESTION_NUMBERS-correct_questions}")
            print(f"Incorrect questions question numbers:{incoorect_question_list} ")
            passed_student_number+=1
        else:            
            print(f"Student {student+1} wasn't passed the exam.")
            print(f"Correct question numbers: {correct_questions}")
            print(f"Incorrect questions numbers: {QUESTION_NUMBERS-correct_questions}")
            print(f"Incorrect questions question numbers:{incoorect_question_list} ")
        print()
        if passed_student_number>=1:
            return False
        else:
            return True

def name_search():
    import a3
    boy_names_list=a3.file_to_list("BoyNames.txt")
    girl_names_list=a3.file_to_list("GirlNames.txt")
        
    name=input("Enter a name: ")
    try:
        boy_names_list.index(name)
        print("The name in the boys list.")
    except ValueError:
        try:
            girl_names_list.index(name)
            print("The name in the girls list.")
        except ValueError:
            print("The name is not on the either list.")

def population_data():
    import a3
    us_population_list=a3.file_to_list("USPopulation.txt")
    annual_change_list=[]
    total=0
    for index in range(len(us_population_list)-1):
        annual_change=int(us_population_list[index+1])-int(us_population_list[index])
        annual_change_list.append(annual_change)
        total+=annual_change  
    print(f"The average annual change in population during the time period: {total/(len(us_population_list)-1):,.2f}")
    print(f"The year with the greatest increase in population during the time period: ",end="") 
    print(f"Year {1950+annual_change_list.index(max(annual_change_list))} , increase {max(annual_change_list):,}")
    print(f"The year with the smallest increase in population during the time period: ",end="") 
    print(f"Year {1950+annual_change_list.index(min(annual_change_list))} , increase {min(annual_change_list):,}")

def 














