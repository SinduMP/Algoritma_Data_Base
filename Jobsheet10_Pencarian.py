#bubble sort
#Searching









# insertion sort
def insertionSort(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      # Move elements of arr[0..i-1], that are greater than key,
      # to one position ahead of their current position
      j = i-1
      while j >=0 and key < arr[j] :
         arr[j+1] = arr[j]
         j -= 1
      arr[j+1] = key
# main
arr = [77, 33, 44, 11, 88, 22, 66, 55]
print('Array before Sorting:')
print (arr)
insertionSort(arr)
print('Array after Sorting:')
print (arr)

# selection sort
import sys 
arr = [77, 33, 44, 11, 88, 22, 66, 55] 
print('Array before Sorting:')
print(arr)
# main
for i in range(len(arr)): 
    min_ele = i 
    for j in range(i+1, len(arr)): 
        if arr[min_ele] > arr[j]: 
            min_ele = j          
    arr[i], arr[min_ele] = arr[min_ele], arr[i] 
  

print('Array after Sorting:')
print (arr)

#selection sort
def selectionSort(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i+1, len(aList)):
            if aList[k] < aList[least]:
                least = k
                 
        swap(aList, least, i)
         
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
# main
arr = [77, 33, 44, 11, 88, 22, 66, 55] 
print('Array before Sorting:')
print(arr)
print('Array after Sorting:')
selectionSort(arr)
print (arr)



#merge sort
def merge_sort(arr):
    size = len(arr)
    if size > 1:
        middle = size // 2
        left_arr = arr[:middle]
        right_arr = arr[middle:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        p = 0
        q = 0
        r = 0
        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
                arr[r] = left_arr[p]
                p += 1
            else:
                arr[r] = right_arr[q]
                q += 1
            r += 1
        while p < left_size:
            arr[r] = left_arr[p]
            p += 1
            r += 1
        while q < right_size:
            arr[r]=right_arr[q]
            q += 1
            r += 1
# main
arr = [11, 31, 7, 41, 101, 56, 77, 2]
print('Array before Sorting:')
print(arr)
merge_sort(arr)
print('Array after Sorting:')
print(arr)


#shell sort
def shell_sort(arr, n):
 
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = arr[i]
            j = i
            while j >= h and arr[j - h] > t:
                arr[j] = arr[j - h]
                j -= h
 
            arr[j] = t
        h = h // 2
 
# main 
arr = [23, 45, 12, 24, 56, 34, 27, 23, 16]
n = len(arr)
print('Array before Sorting:')
print(arr)
shell_sort(arr, n)
print('Array after Sorting:')
print(arr)



def sequentialSearch(target, List):
    position = 0
    global iterations
    iterations = 0
    while position < len(List):
        iterations += 1
        if target == List[position]:
            return position
        position += 1
    return -1

if __name__ == '__main__':
    List = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 1
    answer = sequentialSearch(target, List)
    if answer != -1:
        print('Target found at index :',answer,'in',iterations,'iterations')
    else:
        print('Target not found in the list')
        
# Binary search  
# Python program for recursive binary search.  
# Returns index position of n in list1 if present, otherwise -1  
def binary_search(list1, low, high, n):   
  
   # Check base case for the recursive function  
   if low <= high:  
  
      mid = (low + high) // 2  
  
      # If element is available at the middle itself then return the its index  
      if list1[mid] == n:   
         return mid   
  
      # If the element is smaller than mid value, then search moves  
      # left sublist1  
      elif list1[mid] > n:   
         return binary_search(list1, low, mid - 1, n)   
  
      # Else the search moves to the right sublist1  
      else:   
         return binary_search(list1, mid + 1, high, n)   
  
   else:   
      # Element is not available in the list1  
      return -1  
  
# Test list1ay   
list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 32  
  
# Function call   
res = binary_search(list1, 0, len(list1)-1, n)   
  
if res != -1:   
   print("Element is present at index", str(res))  
else:   
   print("Element is not present in list1")
