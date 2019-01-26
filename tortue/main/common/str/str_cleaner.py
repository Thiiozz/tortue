# coding utf-8

import re


class StrCleaner:
    @staticmethod
    def clean(s) -> str:
        s = StrCleaner.trim_and_lower(s)
        s = StrCleaner.keep_alphanumeric_chars_only(s)
        s = StrCleaner.remove_escaped(s)
        s = StrCleaner.remove_double_white_space(s)

        return s

    @staticmethod
    def trim_and_lower(s) -> str:
        return s.strip().lower()

    @staticmethod
    def keep_alphanumeric_chars_only(s) -> str:
        return re.sub(r'[^a-zA-Z0-9áàâçéèêëíìîïôöûü\s]+', '', s)

    @staticmethod
    def remove_escaped(s) -> str:
        return s \
            .replace('\n', ' ') \
            .replace('\r', ' ') \
            .replace('\t', ' ')

    @staticmethod
    def remove_double_white_space(s) -> str:
        while '  ' in s:
            s = s.replace('  ', ' ')

        return s
