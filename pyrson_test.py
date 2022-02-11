'''
Tests for pyrson personal number validator
'''
import pytest

from pyrson import is_personal_number


def test_sanitation_characters():
    '''Test input with incorrect characters, expected to return False'''
    assert is_personal_number('helloworld') is False
    assert is_personal_number('Robert\'); DROP TABLE Students;--') is False


@pytest.mark.parametrize('number', ['19780202-2389', '19820411-2380'])
def test_known_working_numbers(number):
    '''Test known working personal numbers'''
    assert is_personal_number(number)


def test_null_input():
    '''Test None input, expected to return False'''
    assert is_personal_number(None) is False


def test_empty_number():
    '''Test Empty input, expected to return False'''
    assert is_personal_number('') is False


@pytest.mark.parametrize(
    'number',
    ['1978020-2389', '19780202-238', '24249-23', '14141414141']
)
def test_too_short_number(number):
    '''Test to short number, expected to return False'''
    assert is_personal_number(number) is False


@pytest.mark.parametrize(
    'number',
    ['1978020-238419', '1978110202-21438', '1414141412121141']
)
def test_too_long_number(number):
    '''Test to long number, expected to return False'''
    assert is_personal_number(number) is False


def test_known_bugs():
    '''
    Known bugs: this one will work after input sanitation
    but probably should not
    '''
    assert is_personal_number('hello19820411-2380world')
