"""Binary search using an iterative approach"""
def binary_search(input_array, value):
    first_index = 0
    last_index = len(input_array)
    choosen_index = int((first_index + last_index) / 2)
    while input_array[choosen_index] != value:
        if choosen_index == 0 or choosen_index == len(input_array)-1:
            return -1
        elif input_array[choosen_index] < value:
            first_index = choosen_index
        elif input_array[choosen_index] > value:
            last_index = choosen_index
        choosen_index = int((first_index + last_index) / 2)
    if input_array[choosen_index] == value:
        return choosen_index

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
