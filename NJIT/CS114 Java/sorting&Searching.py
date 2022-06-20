def binarySearch(arr,num):
    left=0
    right=len(arr);
    while left!=right:
        mid=int((left+right)/2);
        if arr[mid]==num: 
            print(str(num)+" is at index: "+str(mid))
            return mid;

        if arr[mid]<num:
            left=mid+1
        else:
            right=mid
    # return None;

def swap(anArr,i,j):
    temp=anArr[i]
    anArr[i]=anArr[j]
    anArr[j]=temp

def bubbleSort(arr):
        #for each loop we look at index i and then iterate 
        # through all other indexes bigger than i and if num at j 
        # is smaller than at i, we switch them.
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                swap(arr,i,j)
        # print(arr)
    print(arr)

def bubbleSort2(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            # print(arr)
            if arr[j]>arr[j+1]:
                swap(arr,j,j+1)
                # print(j,j+1)
        # print(arr)

    print(arr)

def selectionSort(arr):
    for i in range(len(arr)):
        smallest=i
        for j in range(i+1,len(arr)):
            if arr[smallest]>arr[j]:
                smallest=j
        swap(arr,i,smallest)
    print(arr)

lst=[96,34,56,43,1,3,2,4,3,21,96,66,15,125,6]
# bubbleSort(lst)
# bubbleSort2(lst)
selectionSort(lst)
# binarySearch(lst,66)