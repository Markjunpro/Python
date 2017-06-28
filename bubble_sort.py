# bubble sort 2017/6/28 from http://python.jobbole.com/82270/

def bubble_sort(lists):
    count = len(lists)
    for i in range(0,count):
        for j in range(i+1,count):
            if lists[i] > lists[j]:
                lists[i] ,lists[j] = lists[j] ,lists[i]
    return lists

lists = [-25,26,12,46,35,-69,0]
print (lists)
bubble_sort(lists)
print ("bubble sort:" + str(lists))
