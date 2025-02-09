def list_to_file(list_a):
    infile=open("cities.txt","w")
    for i in list_a:
        infile.write(str(i)+"\n")
    infile.close

def file_to_list():
    infile=open("cities.txt","r")
    list_b=infile.readlines()
    infile.close()
    for index in range(len(list_b)):
        list_b[index]=list_b[index].rstrip("\n")
    print(list_b)

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
    list_to_file(list_a)
    file_to_list()
    list_integers=[1,2,3,4]
    for_integers(list_integers)

main()

