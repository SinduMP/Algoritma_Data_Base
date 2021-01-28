#Kasus 1 :
#Anda diminta membuat sebuah program sorting dengan metode buble sort. Mintalah user untuk memasukkan 10 angka. Lalu tampilkan angka-angka tersebut setelah disort baik secara ascending maupun descending

#Layar 1 :
#Masukkan 10 data
#= = = = = = = = = =
#Data ke-1 = 5 		Data ke-6 = 45
#Data ke-2 = 2 		Data ke-7 = 8
#Data ke-3 = 67 		Data ke-8 = 23
#Data ke-4 = 43 		Data ke-9 = 39
#Data ke-5 = 90 		Data ke-10 = 7
#{ket : tampilan ketika mengiput 10 angka}

#Layar 2 :
#5 2 67 43 90 45 8 23 39 7
#Data yang telah diurutkan :
#* * * * * * * * * * * * * *
#Ascending : 2 5 7 8 23 39 43 45 67 90
#Descending : 90 67 45 43 39 23 8 7 5 2
#{ket : tampilan setelah dilakukan bubble sort}




def inputdt():
    data01 = int(input("Data ke -1 ="))
    data02 = int(input("Data ke -2 ="))
    data03 = int(input("Data ke -3 ="))
    data04 = int(input("Data ke -4 ="))
    data05 = int(input("Data ke -5 ="))
    data06 = int(input("Data ke -6 ="))
    data07 = int(input("Data ke -7 ="))
    data08 = int(input("Data ke -8 ="))
    data09 = int(input("Data ke -9 ="))
    data10 = int(input("Data ke -10 ="))
    arr.append(data01)
    arr.append(data02)
    arr.append(data03)
    arr.append(data04)
    arr.append(data05)
    arr.append(data06)
    arr.append(data07)
    arr.append(data08)
    arr.append(data09)
    arr.append(data10)
def dtbase():
    global arr
    arr = []
dtbase()
inputdt()

def cetak01():
    print (arr)
    print('')
    print("Data yang telah diurutkan :")
    sorting()
    print (arr)
    print('')
    ascending()
    print ("Ascending : ",arr)
    descending()
    print ("Descending : ",arr)
def sorting():
    for i in range(1, len(arr)):
      key = arr[i]
      # Move elements of arr[0..i-1], that are greater than key,
      # to one position ahead of their current position
      j = i-1
      while j >=0 and key < arr[j] :
         arr[j+1] = arr[j]
         j -= 1
      arr[j+1] = key
def ascending():
    arr.sort(reverse=False)
def descending():
    arr.sort(reverse=True)
cetak01()
