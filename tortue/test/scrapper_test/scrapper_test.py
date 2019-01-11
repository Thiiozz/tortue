# coding: utf8

from tortue.main.scrapper.scrapper import Scrapper

s = Scrapper()


def test_format_dict_to_model():
    # Given
    data = {'title': 'hello', 'text': 'world'}

    # When
    doc = s.transform_to_doc(data)

    # Then
    assert doc.title == 'hello'


def test_format_with_only_alphanumeric_chars():
    # Given
    data = {'title': 'hello', 'text': '  aBcDefghijklmnopqrstuvwxyz 0123456789 *-+!:/;,?\n'}

    # When
    doc = s.transform_to_doc(data)

    # Then
    assert doc.text == 'abcdefghijklmnopqrstuvwxyz 0123456789'

