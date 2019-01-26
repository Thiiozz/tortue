# coding utf-8

from tortue.main.common.str.str_cleaner import StrCleaner


def test_keep_only_alphanumeric_chars():
    # Given
    s = 'abc!'

    # When
    s = StrCleaner.keep_alphanumeric_chars_only(s)

    # Then
    assert s == 'abc'


def test_trim_and_to_lower():
    # Given
    s = ' aBc '

    # When
    s = StrCleaner.trim_and_lower(s)

    # Then
    assert s == 'abc'


def test_remove_illegal_char_and_format():
    # Given
    s = ' ?aB c! '

    # When
    s = StrCleaner.clean(s)

    # Then
    assert s == 'ab c'


def test_remove_break_line():
    # Given
    s = 'nationalité belge\nelle est'

    # When
    s = StrCleaner.clean(s)

    # Then
    assert s == 'nationalité belge elle est'


def test_double_white_space():
    # Given
    s = 'b    a'

    # When
    s = StrCleaner.clean(s)

    # Then
    assert s == 'b a'