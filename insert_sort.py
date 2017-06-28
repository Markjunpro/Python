def insert_sort(lists):
    #insert sort 2017/6/28
    count = len(lists)
    for i in range(1,count):
        key= lists[i]
        j = i-1
        while j >=0:
            if lists[j] >key:
                lists[j+1] = lists[j]
                lists[j] = key
            j -=1
    return lists

lists= [1,3,5,7,1,-5,52,23,41]
print ("this is the lists:" + str(lists))
insert_sort(lists)
print ("the lists after insert sort :" +str(lists))

    

