def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def rotateArr(arr,k):
    i=0
    for j in range(len(arr)-1,-1,-1):
        if k<=0:
            break
        swap(arr,i,j)
        i+=1
        k-=1
arr=[1,2,3,4,5,6,7]
print(arr)
rotateArr(arr,3)
print(arr)