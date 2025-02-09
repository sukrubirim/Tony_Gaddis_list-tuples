NUM_OF_EMPLOYEES=6
def main():
    hours=[0]*NUM_OF_EMPLOYEES
    for index in range(len(hours)):
        hours[index]=float(input(f"Hours worked by employee {index+1}: "))
    pay_rate=float(input("Hourly payrate: "))
    for index in range(len(hours)):
        gross_pay=hours[index]*pay_rate
        print(f"Gross pay for employee {index+1}: ${gross_pay} ")
main()

    