# Write a function to merge two sorted lists into one sorted list.

list1 = [0, 1, 9, 3, 7, 5]
list2 = [8, 2, 4, 6]

def MergeTwoListIntoOne(ls1, ls2):
    merged_list = []

    list1_sorted = sorted(ls1)
    list2_sorted = sorted(ls2)

    merged_list = list1_sorted+list2_sorted
    merged_list_sorted = sorted(merged_list)
    
    return merged_list_sorted

merged = MergeTwoListIntoOne(list1, list2)
print(merged)