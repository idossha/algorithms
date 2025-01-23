
unsorted_list = [1,20,15,3,5,7,3,10]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left,right):
    merged =  []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

print(merge_sort(unsorted_list))


'''
[1, 20, 15, 3, 5, 7, 3, 10]
         /                        \
[1, 20, 15, 3]               [5, 7, 3, 10]
     /          \                  /         \
[1, 20]      [15, 3]          [5, 7]       [3, 10]
   / \          / \            / \           / \
[1] [20]    [15] [3]        [5] [7]       [3] [10]
   \ /          \ /            \ /           \ /
 [1,20]      [3,15]          [5,7]         [3,10]
         \                /                     /
         [1,3,15,20]             [3,5,7,10]
                     \                  /
                     [1,3,3,5,7,10,15,20]

'''
