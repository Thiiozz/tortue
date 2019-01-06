# coding: utf8

from ..str.str_cleaner import StrCleaner


class RawWikiData:

    def __init__(self, data):
        self.title = ''
        self.text = ''
        self.populate(data)

    def populate(self, data):
        if data['title'] and data['text']:
            self.text = StrCleaner.remove_non_alphanumeric_chars_trim_and_lower(data['text'])
            self.title = StrCleaner.remove_non_alphanumeric_chars_trim_and_lower(data['title'])


