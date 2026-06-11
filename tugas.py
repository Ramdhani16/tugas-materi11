def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][1] < arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


daftar_siswa = [
    ["AHMAD ROSIHAN EFENDI", 60],
    ["ALVIN PRASETYA ANANTA", 81],
    ["AMELIA YULVIANA PUTRI", 79],
    ["ARMAN MAULANA", 62],
    ["DINA MULIANA", 74],
    ["HAIDIR SANJANI", 66],
    ["L. MUH. KHOLIFATUL ARIPI", 70],
    ["M. ASROR RAMDHANI", 85]
]

print("Daftar siswa sebelum diurutkan:")
for siswa in daftar_siswa:
    print(siswa[0], ":", siswa[1])


bubble_sort(daftar_siswa)

print("\nDaftar siswa setelah diurutkan (Berdasarkan Peringkat):")
peringkat = 1
for siswa in daftar_siswa:
    print("Peringkat", peringkat, "-", siswa[0], ":", siswa[1])
    peringkat = peringkat + 1

