from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array}.copy())"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    return min(times)

# Algoritma pengurutan
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    left = merge_sort(array[:midpoint])
    right = merge_sort(array[midpoint:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quicksort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)
    return quicksort(low) + same + quicksort(high)

# Membuat dataset dengan pola berbeda
def create_datasets(size):
    data_sorted = list(range(size))
    data_reversed = list(range(size, 0, -1))
    data_random = [randint(0, size) for _ in range(size)]
    data_same = [size // 2] * size
    return {
        "sorted": data_sorted,
        "reversed": data_reversed,
        "random": data_random,
        "same": data_same,
    }

# Benchmarking
if __name__ == "__main__":
    ARRAY_SIZE = 1000
    datasets = create_datasets(ARRAY_SIZE)
    algorithms = ["bubble_sort", "insertion_sort", "merge_sort", "quicksort"]

    results = {}
    for algo in algorithms:
        results[algo] = {}
        for dataset_type, dataset in datasets.items():
            exec_time = run_sorting_algorithm(algo, dataset)
            results[algo][dataset_type] = exec_time

    # Menampilkan hasil
    for algo, timings in results.items():
        print(f"\nAlgorithm: {algo}")
        for dataset_type, time_taken in timings.items():
            print(f"  {dataset_type:>8}: {time_taken:.6f} seconds")
