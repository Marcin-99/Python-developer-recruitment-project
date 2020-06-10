from number_conditions import check_for_identical_adjacent_digits, are_digits_increasing


def how_many_numbers_do_you_have_to_check():
    possible_numbers = [num for num in range(372**2, 809**2 + 1)
                        if check_for_identical_adjacent_digits(num)
                        and are_digits_increasing(num)]

    return len(possible_numbers)