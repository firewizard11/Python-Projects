def swap(array: list, idx1: int, idx2: int) -> None:
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp