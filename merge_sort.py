# merge sort on 2017/6/28 from http://python.jobbole.com/82270/

def merge(left,right):
    i ,j = 0,0
    result = []
    while i < len(left)  and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left,right)

lists = [2,-5,1,64,-84,12,0,1,-36,14,12,-21]
print (lists)
merge_sort(lists)
print ("merge sort:" + str(lists))

