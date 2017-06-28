# heap sort on 2017/6/28 from http://python.jobbole.com/82270/

def adjust_heap(lists,i,size):
    lchild = 2 * i +1
    rchild = 2 * i +2
    max = i
    if i < size/2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i :
            lists[max],lists[i] = lists[i] ,lists[max]
            adjust_heap(lists,max,size)

def bulid_heap(lists,size):
    for i in range(0,(size/2))[::-1]:
        adjust_heap(lists , i ,size)

def heap_sort(lists):
    size = len(lists)
    bulid_heap(lists,size)
    for  i in range(0,size)[::-1]:
        lists[0] ,lists[i] = lists[i],lists[0]
        adjust_heap(lists,0,i)

lists = [1,-5,1,4,-56,25,-14,95,32,-41,25]
heap_sort(lists)
print (lists)
