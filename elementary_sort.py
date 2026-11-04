
def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n - 1, 0, -1):     
        swapped = False
        for j in range(i):
            comparisons += 1
            if arr[j] > arr[j + 1]:    
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:                
            break

    return comparisons, swaps


def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n - 1):
        smallest = i                   
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[smallest]:
                smallest = j
        if smallest != i:              
            arr[i], arr[smallest] = arr[smallest], arr[i]
            swaps += 1

    return comparisons, swaps


def insertion_sort(arr):
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]                   
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]    
                shifts += 1
                j -= 1
            else:
                break
        arr[j + 1] = key               

    return comparisons, shifts

#test
test_cases = [
    ("A. Random", [29, 10, 14, 37, 13, 5, 22]),
    ("B. Sorted", [1, 2, 3, 4, 5, 6, 7]),
    ("C. Reverse", [7, 6, 5, 4, 3, 2, 1]),
    ("D. Duplicates", [4, 2, 4, 1, 2, 3, 1]),
    ("E1. Empty", []),
    ("E2. Single", [42]),
    ("E3. Two", [2, 1]),
]

for name, data in test_cases:
    print(name, data)

    arr = data[:]                    
    c, s = bubble_sort(arr)
    print("  Bubble   ", arr, "comparisons:", c, "swaps:", s)

    arr = data[:]
    c, s = selection_sort(arr)
    print("  Selection", arr, "comparisons:", c, "swaps:", s)

    arr = data[:]
    c, s = insertion_sort(arr)
    print("  Insertion", arr, "comparisons:", c, "shifts:", s)

    print()