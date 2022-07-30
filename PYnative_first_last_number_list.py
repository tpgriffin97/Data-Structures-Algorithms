numbers_x = [20, 45, 36, 83, 20]
numbers_y = [5, 56, 35, 89, 3, 78]


def first_last(list):

    first_number = list[0]
    last_number = list[-1]

    if first_number == last_number:
        return True
    else:
        return False


print("result is", first_last(numbers_x))
print("result is,", first_last(numbers_y))

