'''
Tests for pyrson personal number validator
'''
import pytest

from pyrson import *


@pytest.mark.parametrize('number', ['19780202-2389', '19820411-2380'])
def test_is_personal_number(number):
    '''Test checksum with known working personal numbers'''
    assert is_personal_number(number)


def test_sanitation_characters():
    '''Test input with incorrect characters, expected to return False'''
    assert remove_non_numerics('helloworld') is ''
    assert remove_non_numerics('Robert\'); DROP TABLE Students;--') is ''


@pytest.mark.parametrize('number', ['19780202-2388', '19820411-2381'])
def test_failing_checksum(number):
    with pytest.raises(Exception):
        checksum(number)


def test_null_input():
    '''Test None input, expected to return False'''
    with pytest.raises(Exception):
        not_null(None)


def test_empty_number():
    '''Test Empty input, expected to return False'''
    with pytest.raises(Exception):
        not_empty(None)


@pytest.mark.parametrize(
    'number',
    ['1978020-2389', '19780202-238', '24249-23', '14141414141',
     '1978020-238419', '1978110202-21438', '1414141412121141']
)
def test_correct_length(number):
    '''Test to short number, expected to return False'''
    with pytest.raises(Exception):
        correct_len(number)


def test_known_bugs():
    '''
    Known bugs: this one will work after input sanitation
    but probably should not
    '''
    assert is_personal_number('hello19820411-2380world')
    assert remove_non_numerics('hello19820411-2380world') == '198204112380'
