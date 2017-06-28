# select sort on 2017/6/28 form http://python.jobbole.com/82270/

def select_sort(lists):
    count = len(lists)
    for i in range(0,count):
        min = i
        for j in range(i+1,count):
            if lists[min] > lists[j]:
                min = j
            lists[min] ,lists[i] = lists[i],lists[min]
        return lists

lists = [2,25,1,-5,45,-56,-12,14]
print (lists)
select_sort(lists)
print ("select sort:" + str(lists))

