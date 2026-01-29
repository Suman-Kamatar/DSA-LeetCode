def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])

    return result

# Example usage:
if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    print("Unsorted array:", data)
    sorted_data = counting_sort(data)
    print("Sorted array:", sorted_data)