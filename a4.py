import matplotlib.pyplot as plt
    
def line_graph():
    x_coords = [0, 1, 2, 3, 4] 
    y_coords = [0, 3, 1, 5, 2]

    plt.plot(x_coords,y_coords,marker="o")
    plt.title("Sales by Year")
    plt.xlabel("Year")
    plt.ylabel("Sales")

    plt.xticks([0,1,2,3,4],list(range(2016,2021)))
    plt.yticks([0,1,2,3,4,5],["$0m","$1m","$2m","$3m","$4m","$5m"])

    plt.grid(True)
    plt.show()

def bar_chart():
    left_edges=[0,10,20,30,40]
    heights=[100,200,300,400,500]
    
    plt.xlim(xmin=-5,xmax=45)
    plt.ylim(ymin=0,ymax=500)
    
    plt.title("Sales by Year")
    plt.xlabel("Year")
    plt.ylabel("Sales")
    plt.xticks([0,10,20,30,40],list(range(2016,2021)))
    plt.yticks([0,100,200,300,400,500],["$0m","$1m","$2m","$3m","$4m","$5m"])
    
    bar_width=10
    plt.bar(left_edges, heights, bar_width,color=('r',"m","c","y","b"))
    plt.show()

def pie_chart():
    values=list(range(20,100,20))
    slice_labels=['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']
    plt.title("Sales by Quarter")
    plt.pie(values,labels=slice_labels,colors=('r', 'g', 'b', 'k'))
    plt.show()

pie_chart()
















    
    
