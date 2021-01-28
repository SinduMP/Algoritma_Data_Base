#Kasus 2
#Output:
#1.	Pada layar komputer ditampilkan nilai dari 100 elemen array yang bertipe integer serta nilai bersifat acak dan berkisar di antara 1 dan 1000.
#2.	Kemudian pada layar komputer ditampilkan pesan yang meminta operator memasukkan nilai yang dicari.
#3.	Jika nilai yang dimaksud tidak ditemukan, pada layar komputer akan ditampilkan pesan 'Nilai tidak ditemukan'. Jika nilai tersebut berhasil ditemukan, pada layar komputer akan ditampilkan pesan 'Nilai ditemukan pada elemen ke X', dengan X adalah indeks elemen array tempat tersimpannya array tersebut. 
#Input:
#1.	Array bertipe integer yang terdiri dari 100 elemen.
#2.	Nilai yang dimasukkan oleh operator untuk dicari di dalam array.



import random
def dtbase():
    global data
    data = []
dtbase()
for i in range(0,100):
    n = random.randint(1,1000)
    data.append(n)
print (data)


def sequentialSearch(target, data):
    position = 0
    global iterations
    iterations = 0
    while position < len(data):
        iterations += 1
        if target == data[position]:
            return position
        position += 1
    return -1
def pencarian():
    if __name__ == '__main__':
        answer = sequentialSearch(target, data)
        if answer != -1:
            print('Target ada pada indeks :',answer,'in',iterations,'iterations')
        else:
            print('Target tidak ada dalam data')
target = int(input("Masukkan nilai target :"))
sequentialSearch(target, data)
pencarian()
