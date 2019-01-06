# coding: utf8

import re

class RawWikiData:

    def __init__(self, data):
        self.title = ''
        self.text = ''
        self.populate(data)

    def populate(self, data):
        if data['title'] and data['text']:
            self.text = self.format_text(data['text'])
            self.title = self.format_text(data['title'])

    def format_text(self, s):
        return re.sub(r'\W+', ' ', s).strip().lower()


