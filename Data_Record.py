
# data base 
def data_base():
    global nama, nim, jurusan, prodi, kelas, alamat, hoby
    nama = []
    nim = []
    jurusan = []
    prodi = []
    kelas = []
    alamat = []
    hoby = []
def tanya():
    tanya1 = input("Apa ingin mengisi data lagi ? (y / t) :")
    if tanya1 == 'y':
        data()
    elif tanya1 == 't':
        cetak()
    else :
        print("Maaf yang anda masukkan salah")
        tanya()
def data():
    print("Masukkan data anda:")
    name = input("Nama    :")
    nama.append(name)
    ni = input("NIM     :")
    nim.append(ni)
    jur = input("Jurusan :")
    jurusan.append(jur)
    prod = input("Prodi   :")
    prodi.append(prod)
    kel = input("Kelas   :")
    kelas.append(kel)
    al = input("Alamat  :")
    alamat.append(al)
    hob = input("Hobi    :")
    hoby.append(hob)
    print('='*22)
    tanya()
def cetak():
    print('-'*115)
    print("No  | Nama   \t| NIM     \t| Jurusan         \t| Prodi           \t| Kelas \t| Alamat      \t| Hoby")
    print('-'*115)
    i = len(nama)
    for n in range(i):
        print(n+1,'. |',nama[n][0:7],'\t|',nim[n][0:8],'\t|',jurusan[n],'\t|',prodi[n],'\t|',kelas[n],'\t|',alamat[n],'\t|',hoby[n])
    print('-'*115)
data_base()
data()
