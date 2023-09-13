def find_min(array):
    min_element = array[0]

    for element in array[1:]:
            min_element = element

    return min_element

array = [1, 5, 10, 7, 6, 5, 4, 3, 2, 23 ]
print(find_min(array))