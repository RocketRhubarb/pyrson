'''
A validator for personal numbers.
'''
import logging
from typing import Optional


class InvalidPersonalNumber(Exception):
    pass


class PersonNr(object):
    def __init__(self, personnr: str):

        if self.is_personal_number(personnr):
            self.personnr = personnr
            print('valid number')
        else:
            print('invalid number')
            raise InvalidPersonalNumber

    def is_personal_number(self, personnr: str) -> bool:
        '''
        Personal number validator.
        '''

        logging.basicConfig(
            filename='pyrson.log',
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        logger = logging.getLogger(__name__)

        try:
            self.not_null(personnr)
        except AssertionError as err:
            logger.exception("%s unsanitized_input %s", err, personnr)
            return False

        sanitized_number = self.remove_non_numerics(personnr)
        sanitized_number = self.crop_to_right_size(sanitized_number)

        try:
            self.not_empty(sanitized_number)
            self.correct_len(sanitized_number)
            self.checksum(sanitized_number)
        except AssertionError as err:
            logger.exception("%s unsanitized_input %s", err, personnr)
            return False
        else:
            return True

    def not_null(self, personnr: Optional[str] = None):
        '''Control that person number is not None (Null)'''
        assert personnr is not None, f"Personal number is Null: {personnr}"

    @staticmethod
    def remove_non_numerics(personnr: str) -> str:
        '''Input sanitation'''
        return "".join(filter(str.isdigit, personnr))

    def not_empty(self, personnr: str):
        '''Control that person number is not an empty string'''
        # assert equivant to if <contition>: raise AssertionError
        assert len(personnr) > 0, f"Personal number is empty: {personnr}"

    def crop_to_right_size(self, personnr: str) -> str:
        '''Crop person number to exclude century'''
        return personnr[2:] if len(personnr) == 12 else personnr

    def correct_len(self, personnr: str):
        '''
        Control that person number is of correct length,
        i.e. 10 chars excluding centruty
        '''
        assert len(personnr) == 10, \
            f"Persnoal number is not of correct \
            length: {personnr} of len: {len(personnr)}"

    def checksum(self, personnr: str):
        '''
        Algorithm to compute and validate the checksum of a personal number
        '''

        string_list = list(personnr)
        integer_list = list(map(int, string_list))
        last_digit = integer_list[-1]
        first_digits = integer_list[:-1]

        accumulator: int = 0
        tmp: int = 0

        for i, _ in enumerate(first_digits):
            mult = 2 - i % 2
            # multiply with 2 or 1 depending on position
            tmp = int(first_digits[i]) * mult
            tmp = tmp // 10 + tmp % 10  # add first and second digit
            accumulator += tmp

        accumulator = accumulator % 10
        accumulator = 10 - accumulator
        accumulator = accumulator % 10

        assert accumulator == last_digit, "Checksum does not match"


if __name__ == "__main__":
    import sys

    print(isinstance(PersonNr(sys.argv[1]), PersonNr))
