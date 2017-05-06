print (" welcome Here is my SJF ")

p=[]
total=0
t=0
int(t)
int(total)
wtt=0
int(wtt)
bt=[]
ft=[]
tat=[]
#arrival time is 0 for all process
i=0
print("enter the number of processes")
n=input()

for i in range (0,int(n)):
        p.append([])
        p[int(i)].append(0)
        #p[int(i)].append(input("Enter arrival time:"))
        p[int(i)].append(input("Enter burst time:"))
        num1 = int(p[i][1])
        bt.append(num1)
        t=int(num1)+t

p.sort(key=lambda p:p[1])
#ft.append(bt[0])
for i in range(0,int(n)):
        num1 = int(p[i][1])
        total=int(num1)+total
        
        ft.append(total)
        
for i in range(0,int(n)):
        a=p[int(i)][0]
        wtt=((ft[i])-int(a))
        tat.append(wtt)
    
print ("Arival time","---","Burst time---turnaround time----finish time")

for i in range(0,int(n)): 
    print("P",int(i+1),"  ",p[i][0],"            ",p[i][1],"         ",tat[int(i)],"              ",ft[int(i)])

    
       
print("Total time taken to run all processes : ")	
print (t)
#print("Average turn around time:")
#print(sum(tat/len(n))
