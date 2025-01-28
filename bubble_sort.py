

def bubble_sort(arr,order = 0):

    if(order==0):
        for i in range(0,len(arr)-1):
            flag = 0
            for j in range(0,len(arr)-1):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    flag = 1
            if(flag==0):
                break
    else:
        for i in range(0,len(arr)-1):
            flag = 0
            for j in range(0,len(arr)-1):
                if(arr[j]<arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    flag = 1
            if(flag==0):
                break
    return arr


arr = []
while(True):
    try:
        n = int(input("Enter Number (Enter other than number to exit): "))
        arr.append(n)

    except:
        break

print (f"Array Before sorting : {arr}")
print (f"Array sorted in assending order : {bubble_sort(arr)}")
print (f"Array sorted in decending order : {bubble_sort(arr,1)}")
