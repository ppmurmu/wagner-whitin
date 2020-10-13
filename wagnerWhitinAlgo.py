import numpy as np
demand=[20,50,10,50,50,10,20,40,20,30]
h=1    #carrying cost
a=100  #set-up cost
opti=[0]
matrix=np.zeros([10, 10]) 
def value(i,j):    #calculating each week cost
    s=opti[j-1]+a
    n=i-j
    for k in range(1,n+1):
        s=s+k*h*demand[j]
        j=j+1
    return s
def minimumOfWeek(i):
    min=matrix[0][i-1]
    for j in range(0,i):
        if(matrix[j][i-1]<min):
            min=matrix[j][i-1]
    return min
            
def wagner():
    for k in range(1,len(demand)+1):
        for l in range(k,0,-1):
            t1=value(k,l)
            matrix[l-1][k-1]=t1
        t=minimumOfWeek(k)
        opti.append(t)
wagner()
print("Wagner–Whitin solution: ") 
print(matrix)
print("Optimal Cost Z*= ", opti[len(demand)])

period=(int)(input("Input period: "))
matrix=np.zeros([period, period])
demand=[]
for i in range(0,period):
    demand.append(int(input("Enter demand for " + str(i+1) + " :")))
print("Your demand list: ",demand)
h=(int)(input("Enter carrying cost: "))
a=(int)(input("Enter set-up cost: "))
opti=[0]
wagner()
print("Wagner–Whitin solution: ") 
print(matrix)
print("Optimal Cost Z*= ", opti[len(demand)])
