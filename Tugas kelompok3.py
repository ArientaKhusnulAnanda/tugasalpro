from random import randint, uniform
from timeit import timeit

# Generate financial transaction data
def generate_financial_data(size):
    """Generate financial transaction data."""
    return [{"id": i, "amount": round(uniform(1, 10000), 2)} for i in range(size)]

# Bubble Sort
def bubble_sort_transactions(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j]["amount"] > array[j + 1]["amount"]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

# Insertion Sort
def insertion_sort_transactions(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j]["amount"] > key_item["amount"]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

# Merge Sort
def merge_sort_transactions(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    left = merge_sort_transactions(array[:midpoint])
    right = merge_sort_transactions(array[midpoint:])
    return merge_transactions(left, right)

def merge_transactions(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["amount"] <= right[j]["amount"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quicksort_transactions(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]["amount"]
    for item in array:
        if item["amount"] < pivot:
            low.append(item)
        elif item["amount"] == pivot:
            same.append(item)
        else:
            high.append(item)
    return quicksort_transactions(low) + same + quicksort_transactions(high)

# Benchmarking
if __name__ == "__main__":
    TRANSACTION_COUNT = 500  # Jumlah data transaksi
    transactions = generate_financial_data(TRANSACTION_COUNT)

    algorithms = {
        "Bubble Sort": bubble_sort_transactions,
        "Insertion Sort": insertion_sort_transactions,
        "Merge Sort": merge_sort_transactions,
        "Quick Sort": quicksort_transactions,
    }

    print(f"Benchmarking Sorting Algorithms on {TRANSACTION_COUNT} Financial Transactions:")
    for name, func in algorithms.items():
        exec_time = timeit(lambda: func(transactions.copy()), number=1)
        print(f"{name}: {exec_time:.6f} seconds")
