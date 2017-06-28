#shell sort 2017/6/28 from http://python.jobbole.com/82270/

def shell_sort(lists):
    count = len(lists)
    step = 2
    group = count/step
    while group >0:
        for i in range(0,group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists

lists = [1,5,-6,3,-7,52,-65]
print (lists)
shell_sort(lists)
print ("shell sort:" + str(lists))

