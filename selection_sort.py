
def selection_sort(array):

    for i in range(0,len(array)):
        min_ele = i
        for j in range(i,len(array)):
            if(array[min_ele]>array[j]):
                min_ele = j
        
        temp = array[min_ele]
        array[min_ele] = array[i]
        array[i] = temp


arr = [1,55,5,2,2,98,8,46,56,20,25,50,16,89,32,48,75]

print(arr)
selection_sort(arr)
print(f"Sorted array : {arr}")