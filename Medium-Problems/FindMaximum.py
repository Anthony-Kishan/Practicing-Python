# Write a function that finds the maximum number in a list.

my_ls = [5, 1, 0, 48, 9, 3, 9, 10, 8, 4, 7, 6]

def MaxInList(ls):
    max = my_ls[0]
    for i in ls:
        if i > max:
            max = i

    print(f"The maximum number of the list is {max}")

MaxInList(my_ls)