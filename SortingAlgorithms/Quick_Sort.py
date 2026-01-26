def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


def partition(arr, low, high):
    pivot = arr[high]     # last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
if __name__ == "__main__":
    sample_array = [10, 7, 8, 9, 1, 5]
    quick_sort(sample_array, 0, len(sample_array) - 1)
    print("Sorted array is:", sample_array)