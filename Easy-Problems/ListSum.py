# Write a function that takes a list of numbers and returns the sum

num_ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def SumListItems(ls):
    j=0
    for i in range(len(ls)):
        j += ls[i]
        
    print (j)

SumListItems(num_ls)