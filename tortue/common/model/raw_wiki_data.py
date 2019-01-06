# coding: utf8


class RawWikiData:

    def __init__(self, data):
        self.title = ''
        self.text = ''
        self.populate(data)

    def populate(self, data):
        if data['title'] and data['text']:
            self.text = data['text']
            self.title = data['title']
