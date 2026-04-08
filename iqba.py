def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


nama = "iqbal"

data = nama.replace(" ", "").upper()

sorted_data = sorted(data)

target = 'A'

hasil = binary_search(sorted_data, target)

print("Data setelah diurutkan:", sorted_data)

if hasil != -1:
    print(f"Huruf '{target}' ditemukan pada index ke-{hasil}")
else:
    print(f"Huruf '{target}' tidak ditemukan")