# Bubble Sort 
import random

array = [random.randint(1,99) for i in range(20)]

print (array) # Unsorted

sort = False
while sort == False:
    sort = True # So that the loop stops if no swaps are made 
    for i in range (1, len(array)):
        if array[i-1] > array[i]:
            temp = array[i]
            array[i] = array[i-1]
            array[i-1] = temp
            sort = False

print (array) # Sorted
