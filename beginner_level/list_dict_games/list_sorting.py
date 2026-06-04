# Implement a basic Bubble Sort to understand sorting logic

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

list_entry = list(map(int, input("Enter numbers separated by space: ").split()))
sorted_list = bubble_sort(list_entry)
print("Sorted list:", sorted_list)