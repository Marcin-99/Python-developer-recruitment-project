def check_for_identical_adjacent_digits(number):
    num_of_groups = 0
    sequence = []

    for digit in str(number):
        if digit in sequence:
            sequence.append(digit)
        else:
            num_of_groups += 1 if len(sequence) >= 2 else 0
            sequence.clear()
            sequence.append(digit)

    num_of_groups += 1 if len(sequence) >= 2 else 0

    return True if num_of_groups >= 2 else False


def are_digits_increasing(number):
    num_str = str(number)

    for i in range(1, len(num_str)):
        if int(num_str[i]) < int(num_str[i-1]):
            return False

    return True
