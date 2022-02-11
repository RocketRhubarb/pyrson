'''
A validator for personal numbers.
'''
import logging
from typing import Optional


def not_empty(personnr: str):
    # assert equivant to if <contition>: raise AssertionError
    assert len(personnr) > 0, f"Personal number is empty: {personnr}"


def not_null(personnr: Optional[str] = None):
    assert personnr is not None, f"Personal number is Null: {personnr}"


def correct_len(personnr: str):
    assert len(personnr) == 10, \
        f"Persnoal number is not of correct \
        length: {personnr} of len: {len(personnr)}"


def checksum(personnr: str):

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

    assert accumulator == last_digit, "Checksum does not match"


def remove_non_numerics(personnr: str) -> str:
    return "".join(filter(str.isdigit, personnr))


def crop_to_right_size(personnr: str) -> str:
    return personnr[2:] if len(personnr) == 12 else personnr


def is_personal_number(personnr: str) -> bool:
    '''
    Personal number validator.
    '''

    # run tests
    try:
        not_null(personnr)
    except AssertionError as err:
        logger.exception("%s unsanitized_input %s", err, personnr)
        return False

    # input sanitation
    sanitized_number = remove_non_numerics(personnr)
    sanitized_number = crop_to_right_size(sanitized_number)

    # run tests
    try:
        not_empty(sanitized_number)
        correct_len(sanitized_number)
        checksum(sanitized_number)
    except AssertionError as err:
        logger.exception("%s unsanitized_input %s", err, personnr)
        return False
    else:
        return True


if __name__ == "__main__":
    logging.basicConfig(
        filename='pyrson.log',
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)
    # logger.info("info level")

    numbers = [
        "",
        "19780202-2389",
        "19780202-2389",
        "197802022389",
        "7802022389",
        "802022389",
        None,
        "19820411-2380"
    ]

    for number in numbers:
        print(number, is_personal_number(number))
