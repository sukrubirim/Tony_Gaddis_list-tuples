def get_scores():
    count=1
    another="y"
    scores=[]
    while another=="y" or another=="Y":
        while True:
            try:
                grade=float(input(f"Enter your exam{count} grade: "))
                break
            except ValueError:
                print("Invalid value try again.")
        scores.append(grade)
        count+=1
        another=input("Another (y,Y,n,N): ")
        while another not in ["y","Y","n","N"]:
            another=input("Another (y,Y,n,N): ")     
    return scores

def calculate_average(scores):
    total=0.0
    for i in scores:
        total+=i 
    lowest_grade=min(scores)
    average=(total-lowest_grade)/(len(scores)-1)
    return average

def main():
    scores=get_scores()
    average=calculate_average(scores)
    print(f"Your average grade without lowest grade: {average}")

if __name__=="__main__":
    main()
