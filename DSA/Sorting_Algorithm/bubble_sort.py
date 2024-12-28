from helper_functions import swap

def bubble_sort_basic(array: list) -> None:
    n = len(array)

    for i in range(n - 1):
        for j in range(n - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)


def bubble_sort_I(array: list) -> None:
    n = len(array)
    mark = n - 1

    for i in range(n - 1):
        for j in range(mark):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
            
        mark -= 1


if __name__ == '__main__':
    test_array = [5, 1, 20, 18, 34, 6]
    test_array_2 = test_array.copy()
    test_array_3 = test_array.copy()
    
    print('====== Test ======')
    print(f'Test Array: {test_array}')

    bubble_sort_basic(test_array)

    print('=== Bubble Sort Basic ===')
    print(f'Sorted Array: {test_array}')

    bubble_sort_I(test_array_2)

    print('=== Bubble Sort I ===')
    print(f'Sorted Array: {test_array_2}')
    
