def mario(he,sh):
    
    sh=str(sh)
    lst=[]
    for i in range(he-1):
        lst.append(' ')
        if i==he-2:
            lst.append(sh)
    lst.append(' ')
    lst.append(sh)
    for i in range(he-1):
        lst.append(' ')
    print(''.join(lst))
    for i in range(he-1):
        lind=(lst.index(sh))-1
        rind=(lind+1)*-1
        del lst[lind]
        lst.insert(lind,sh)
        del lst[rind]
        lst.insert(rind,sh)
        print(''.join(lst))
mario(10,"*")
