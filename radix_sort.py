# radix sort on 2017/6/28  from http://python.jobbole.com/82270/

import math
def radix_sort(lists,radix= 10):
    k = int (math.ceil(math.log(max(lists),radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1,k+1):
        for j in lists:
            bucket[j%(radix**(i))//(radix**(i-1))].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists

lists = [1,2,25,-26,12,24,-36,21,56]
print (lists)
radix_sort(lists)
print (lists)

