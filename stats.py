import math

def getData(lst):
    lst.sort()
    print(lst)
    avg=sum(lst)/len(lst)
    median=lst[len(lst)//2]
    if (len(lst)//2)==0:
        mid=len(lst)//2
        median=(lst[mid-1]+lst[mid])/2
        
    variance=sum([(i-avg)**2 for i in lst])/(len(lst)-1)
    sd=math.sqrt(variance)
    #q1Pos=((len(lst)+1)/4)
    #q2Pos=((2*(len(lst)+1))/4)
    #q3Pos=((3*(len(lst)+1))/4)
#
    #iqr=lst[int(q3)-1]-lst[int(q1)-1]
    #lowBound=lst[int(q1)]-(1.5*iqr)
    #upprerBound=q3+(1.5*iqr)
    print(f"\nMedian: {median}")
    print(f"Average: {avg}")
    print(f"Standard Deviation: {sd}")
    print(f"Variance: {variance}\n")
    #print(f"Q1:[pos:{q1},data:{lst[int(q1)-1]}]  Q2:[pos:{q2},data:{lst[int(q2)-1]}] Q3:[pos:{q3},data:{lst[int(q3)-1]}]")
    #print(f"IQR: {iqr}")
    #print(f"Outliers: Lower than {lowBound}, More than {upprerBound}")
    #totalOutliers=0
    #for i in range(len(lst)):
        #if lst[i]<lowBound or lst[i]>upprerBound:
            #totalOutliers+=1
            #print(f"{i}) {lst[i]}")
    #print(f"totalOutliers: {totalOutliers}") 



#lst="450 450 390 483 506 548 477 1172 1219 1104 1106 976 1176 1273 1306 1446 1611 1673 1800 2840 3250 3175 3382 1965 2499 2720 2642"
#lst="88.5 98.8 89.6 92.2 92.7 91.8 91.0 91.0 94.7 88.3 90.4 83.4 87.9 88.4 87.5 90.9 84.3 90.4 91.6 91.0 93.0 92.6 87.8 89.9 90.1 91.2 90.7 88.2 94.4 93.7 88.3 91.8 89.0 90.6 88.6 88.5 90.4 96.5 89.2 89.7 89.8 92.2 88.3 93.3 91.2 84.3 92.3 92.2 91.6 87.7 94.2 87.4 91.2 93.2 88.9   90.3 91.1 85.3 91.1 86.7 88.6 89.8   90.0 86.7 90.1 90.5 94.2 88.7 92.7   91.5 93.4 89.3 100.3 90.8 92.7 93.3   89.9 96.1 91.1 87.6 90.1 89.3 86.7"

lst="87.3 98.8 87.8 91.1 92.9 92.1 90.6 89.9 93.7 89.7 91.2 83.6 89.0 88.3 87.5 90.8 83.1 89.6 91.8 91.5 93.3 92.3 87.7 89.5 89.3 91.3 90.4 87.3 94.6 93.6 88.9 90.3 88.9 90.9 88.0 89.0 90.7 96.6 90.5 88.5 89.9 92.5 88.0 94.6 91.2 84.8 91.8 93.3 92.2 85.8 94.9 88.6 91.5 93.7 90.4   90.1 89.6 85.6 91.3 87.2 88.9 91.0   91.2 85.0 90.9 90.8 95.2 87.7 92.6   90.2 94.4 89.9 100.9 91.5 92.5 93.5   89.8 97.9 90.4 87.3 89.7 89.4 85.6"
lst="62	64	66	67	65	68	61	65	67	65	64	63	67 68	64	66	68	69	65	67	62	66	68	67	66	65 69	65	70	65	67	68	65	63	64	67	67"
lst="1.62 1.95 2.65 2.31 3.07 3.29 2.54 1.90"
lst=lst.split()
print(len(lst))

lst=[float(i) for i in lst]

getData(lst)
