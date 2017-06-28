# quick sort on 2017/6/28 from http://python.jobbole.com/82270/

def quick_sort(lists,left,right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists,low,left - 1)
    quick_sort(lists,left + 1,high)
    return lists

lists = [1,-2,-56,24,12,0]
print (lists)
quick_sort(lists,0,len(lists)-1)
print ("quick sort:" + str(lists))


    
