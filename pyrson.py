'''
A validator for personal numbers.
'''


def not_empty(personnr: str):
    assert len(personnr) > 0, f"Personal number is empty: {personnr}"


def not_null(personnr: str):
    assert personnr != None, f"Personal number is Null: {personnr}"


def correct_len(personnr: str):
    assert len(
        personnr) == 10, f"Persnoal number is not of correct length: {personnr} of len: {len(personnr)}"


def is_personal_number(personnr: str):

    string_list = list(personnr)
    integer_list = list(map(int, string_list))
    last_digit = integer_list[-1]
    first_digits = integer_list[:-1]

    accumulator: int = 0
    tmp: int = 0

    for i in range(0, len(first_digits)):
        mult = 2 - i % 2
        # multiply with 2 or 1 depending on position
        tmp = int(first_digits[i]) * mult
        tmp = tmp // 10 + tmp % 10  # add first and second digit
        accumulator += tmp

    accumulator = accumulator % 10
    accumulator = 10 - accumulator
    accumulator = accumulator % 10

    print(accumulator, last_digit)

    assert accumulator == last_digit, "Not a valid personal number"


def remove_non_numerics(personnr: str) -> str:
    return "".join(filter(str.isdigit, number))


def crop_to_right_size(personnr: str) -> str:
    return personnr[2:] if len(personnr) == 12 else personnr


def personal_number_validator(number: str):
    '''
    Personal number validator.
    '''
    not_null(number)
    not_empty(number)

    number = remove_non_numerics(number)
    number = crop_to_right_size(number)

    correct_len(number)
    is_personal_number(number)


if __name__ == "__main__":
    numbers = [
        "",
        "19780202-2389",
        "19780202-2389",
        "197802022389",
        "7802022389",
        "802022389",
        # None,
        "19820411-2380"
    ]

    for number in numbers:
        personal_number_validator(number)
