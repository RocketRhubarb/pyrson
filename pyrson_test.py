'''
Tests for pyrson personal number validator
'''
import pytest

from pyrson import InvalidPersonalNumber, PersonNr


@pytest.mark.parametrize('number', ['197802022389', '198204112380'])
def test_is_personal_number(number):
    '''Test checksum with known working personal numbers'''
    assert isinstance(PersonNr(number), PersonNr)


@pytest.mark.parametrize('number', ['197802022388', '198204112381'])
def test_instantiating_class_wrong_num(number):
    '''Test examples instantiating class with incorrect number'''
    with pytest.raises(InvalidPersonalNumber):
        PersonNr(number)


@pytest.mark.parametrize('number', ['197802022387', '198204112381'])
def test_failing_checksum(number):
    '''Test examples of failing checksums'''
    personnr = PersonNr('197802022389')
    with pytest.raises(Exception):
        personnr.checksum(number)


def test_null_input():
    '''Test None input, expected to return False'''
    personnr = PersonNr('197802022389')
    with pytest.raises(Exception):
        personnr.not_null(None)


def test_empty_number():
    '''Test Empty input, expected to return False'''
    personnr = PersonNr('197802022389')
    with pytest.raises(Exception):
        personnr.not_empty(None)


@pytest.mark.parametrize('number', ['147802022387', '218204112381'])
def test_failing_checksum(number):
    '''Test examples of failing checksums'''
    personnr = PersonNr('197802022389')
    with pytest.raises(Exception):
        personnr.invalid_date_range(number)


@pytest.mark.parametrize(
    'number',
    ['19780202389', '19780202238', '2424923', '14141414141',
     '1978020238419', '197811020221438', '1414141412121141']
)
def test_correct_length(number):
    '''Test to short number, expected to return False'''
    personnr = PersonNr('197802022389')
    with pytest.raises(Exception):
        personnr.correct_len(number)


def test_crop():
    '''Test cropping'''
    personnr = PersonNr('197802022389')
    assert personnr.crop_to_right_size('YYYYMMDDXXXX') == 'YYMMDDXXXX'


@pytest.mark.parametrize('number', ['19780202-2389', '19820411-2380', 'hello198204112380world'])
def test_known_bugs(number):
    '''
    Non-digit numbers in personal number, only allows YYYYMMDDXXXX
    '''
    with pytest.raises(InvalidPersonalNumber):
        PersonNr(number)
