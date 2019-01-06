# coding: utf8

from ..scrapper.scrapper import Scrapper


def test_format_dict_to_model():
    # Given
    data = {'title': 'Hello', 'text': 'world'}
    s = Scrapper()

    # When
    doc = s.transform_to_doc(data)

    # Then
    assert doc.title == 'Hello'
