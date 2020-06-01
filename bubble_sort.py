# Author: Nguyen L.
# Date:   Apr 27, 2020
# Bubble Sort Algorithm


# bubble sort algorithm function
def bubbleSort(my_list):

    for i in range(len(my_list)):

        for j in range(0, len(my_list)-1): 

            if my_list[j] > my_list[j+1]:
                t = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = t
    
    return my_list

my_list = [4, 30, 22, 27, 41, 1, 5, 80]
print("Before sorted: ", end='')
print(my_list)
print("After sorted: ", end='')
print(bubbleSort(my_list))