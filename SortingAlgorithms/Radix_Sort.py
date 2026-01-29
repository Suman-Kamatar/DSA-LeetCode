def radix_sort(arr):
    max_num = max(arr)
    exp = 1  # 1, 10, 100...

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # count digits
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # prefix sum
    for i in range(1, 10):
        count[i] += count[i - 1]

    # build output (right to left → stability)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # copy back
    for i in range(n):
        arr[i] = output[i]

# Example usage:
if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Unsorted array:", data)
    radix_sort(data)
    print("Sorted array:", data)