'''
Tests for pyrson personal number validator
'''
import pytest

from pyrson import InvalidPersonalNumber, PersonNr


@pytest.mark.parametrize('number', ['19780202-2389', '19820411-2380'])
def test_is_personal_number(number):
    '''Test checksum with known working personal numbers'''
    assert isinstance(PersonNr(number), PersonNr)


@pytest.mark.parametrize('number', ['19780202-2388', '19820411-2381'])
def test_instantiating_class_wrong_num(number):
    '''Test examples instantiating class with incorrect number'''
    personnr = PersonNr('19780202-2389')
    with pytest.raises(InvalidPersonalNumber):
        PersonNr(number)


def test_sanitation_characters():
    '''Test input with incorrect characters, expected to return False'''
    assert PersonNr.remove_non_numerics('helloworld') == ''
    assert PersonNr.remove_non_numerics(
        'Robert\'); DROP TABLE Students;--') == ''


@pytest.mark.parametrize('number', ['19780202-2388', '19820411-2381'])
def test_failing_checksum(number):
    '''Test examples of failing checksums'''
    personnr = PersonNr('19780202-2389')
    with pytest.raises(Exception):
        personnr.checksum(number)


def test_null_input():
    '''Test None input, expected to return False'''
    personnr = PersonNr('19780202-2389')
    with pytest.raises(Exception):
        personnr.not_null(None)


def test_empty_number():
    '''Test Empty input, expected to return False'''
    personnr = PersonNr('19780202-2389')
    with pytest.raises(Exception):
        personnr.not_empty(None)


@pytest.mark.parametrize(
    'number',
    ['1978020-2389', '19780202-238', '24249-23', '14141414141',
     '1978020-238419', '1978110202-21438', '1414141412121141']
)
def test_correct_length(number):
    '''Test to short number, expected to return False'''
    personnr = PersonNr('19780202-2389')
    with pytest.raises(Exception):
        personnr.correct_len(number)


def test_crop():
    '''Test cropping'''
    personnr = PersonNr('19780202-2389')
    assert personnr.crop_to_right_size('YYYYMMDDXXXX') == 'YYMMDDXXXX'


def test_known_bugs():
    '''
    Known bugs: this one will work after input sanitation
    but probably should not
    '''
    personnr = PersonNr('19780202-2389')
    assert personnr.is_personal_number('hello19820411-2380world')
    assert personnr.remove_non_numerics(
        'hello19820411-2380world') == '198204112380'
