def SumOfPrevious(theLst,ind):
    hasSumInLst=theLst[ind]
    for num in theLst[ind+1:]:
        potentialSum=num
        for num2 in theLst[ind+2:]:
            if potentialSum+num2==hasSumInLst:
                print(theLst[ind+1:])
                print(num,num2)
                print(ind,hasSumInLst)
                return True
    if len(theLst) != ind-1:
        return SumOfPrevious(theLst,ind+1)
    return False
def main():
    # num=input("Enter num: ")
    # lst=input("Enter numbers: ").split(" ")
    lst=[9 ,8 ,7 ,6 ,5 ,4 ,3]
    print(SumOfPrevious(lst,0))

main()