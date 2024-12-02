from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Setup kode untuk impor fungsi (jika diperlukan)
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""
    
    # Statement yang akan dieksekusi (algoritma pengurutan)
    stmt = f"{algorithm}({array})"
    
    # Mengukur waktu eksekusi sebanyak 3 kali pengulangan
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    
    # Mencetak waktu eksekusi minimum
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


if __name__ == "__main__":
    # Panjang array yang akan diuji
    ARRAY_LENGTH = 1000
    # Membuat array acak
    array = [randint(0, 1000) for _ in range(ARRAY_LENGTH)]
    # Mengukur waktu eksekusi fungsi sorted
    run_sorting_algorithm(algorithm="sorted", array=array)
    

############################################################################# Algoritma Bubble Sort

# Implementasi Bubble Sort
def bubble_sort(array):
    n = len(array)
    # Loop untuk iterasi array
    for i in range(n):
        already_sorted = True
        # Loop untuk membandingkan elemen bersebelahan
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # Menukar elemen jika tidak dalam urutan yang benar
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        # Jika sudah terurut, hentikan loop
        if already_sorted:
            break
    return array


# Kode utama
if __name__ == "__main__":
    # Mengatur panjang array
    ARRAY_LENGTH = 1000
    # Membuat array acak
    array = [randint(0, 1000) for _ in range(ARRAY_LENGTH)]
    # Mengukur waktu eksekusi Bubble Sort
    run_sorting_algorithm(algorithm="bubble_sort", array=array)

########################################################################### Algoritma Insertion Sort

# Implementasi Insertion Sort
def insertion_sort(array):
    # Loop dari elemen kedua hingga akhir array
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        # Pindahkan elemen yang lebih besar ke kanan
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        # Menempatkan key_item pada posisi yang benar
        array[j + 1] = key_item
    return array

# Kode utama
if __name__ == "__main__":
    # Mendefinisikan panjang array
    ARRAY_LENGTH = 1000
    # Membuat array dengan panjang ARRAY_LENGTH berisi nilai acak antara 0 dan 999
    array = [randint(0, 1000) for _ in range(ARRAY_LENGTH)]
    # Memanggil fungsi untuk menjalankan algoritma Insertion Sort dan mengukur waktu eksekusinya
    run_sorting_algorithm(algorithm="insertion_sort", array=array)

########################################################################################################### Algoritma Merge Sort
# Fungsi untuk menggabungkan dua bagian yang sudah terurut
def merge(left, right):
    result = []
    i = j = 0
    # Menggabungkan elemen dari left dan right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Menambahkan sisa elemen yang belum diproses
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Implementasi Merge Sort
def merge_sort(array):
    # Jika array memiliki kurang dari dua elemen, kembalikan array
    if len(array) < 2:
        return array
    # Membagi array menjadi dua bagian
    midpoint = len(array) // 2
    # Mengurutkan setiap bagian secara rekursif
    left = merge_sort(array[:midpoint])
    right = merge_sort(array[midpoint:])
    # Menggabungkan dua bagian yang sudah terurut
    return merge(left, right)

# Kode utama
if __name__ == "__main__":
    # Membuat array acak
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print("Array sebelum diurutkan:", array)

    # Menjalankan algoritma pengurutan
    run_sorting_algorithm(algorithm="merge_sort", array=array)

################################################################################## Algoritma Quick Sort
from random import randint

# Implementasi Quick Sort
def quicksort(array):
    # Jika array memiliki kurang dari dua elemen, kembalikan array
    if len(array) < 2:
        return array
    # Membuat tiga list: low, same, dan high
    low, same, high = [], [], []
    # Memilih pivot secara acak
    pivot = array[randint(0, len(array) - 1)]
    # Mengelompokkan elemen berdasarkan pivot
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)
    # Mengurutkan bagian low dan high secara rekursif
    return quicksort(low) + same + quicksort(high)

#Mengukur Waktu Eksekusi Quick Sort
if __name__ == "__main__":
    # Membuat array acak dengan 10.000 elemen
    array = [randint(0, 1000) for _ in range(10000)]
    # Mengukur waktu eksekusi Quick Sort
    run_sorting_algorithm(algorithm="quicksort", array=array)
