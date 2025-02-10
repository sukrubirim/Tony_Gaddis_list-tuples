def list_to_file(list_a,file_name):
    infile=open(file_name,"w")
    for i in list_a:
        infile.write(str(i)+"\n")
    infile.close
    
def file_to_list(file_name):
    infile=open(file_name,"r")
    list_x=infile.readlines()
    infile.close()
    for index in range(len(list_x)):
        list_x[index]=list_x[index].rstrip("\n")
    return list_x

def for_integers(list_integers):
    condition=True
    for index in range(len(list_integers)):
        if type(list_integers[index])==int:
            condition=True
        else:
            condition=False
            break
    if condition :
        infile=open("integers.txt","w")
        for item in list_integers:
            infile.write(str(item)+"\n")
        infile.close()
    else:
        list_to_file(list_integers)
        file_to_list()
            
def main():
    list_a=["newyork","boston","atlanta","dallas"]
    file_name="cities.txt"
    list_to_file(list_a,file_name)
    list_b=file_to_list(file_name)
    print(list_b)
    list_integers=[1,2,3,4]
    for_integers(list_integers)

if __name__=="__main__":
    main()

