# coding utf-8

import re


class StrCleaner:
    @staticmethod
    def keep_alphanumeric_chars_only(s):
        return re.sub(r'[^\s\w_]+', '', s)

    @staticmethod
    def trim_and_lower(s):
        return s.strip().lower()

    @staticmethod
    def remove_non_alphanumeric_chars_trim_and_lower(s):
        return StrCleaner.trim_and_lower(StrCleaner.keep_alphanumeric_chars_only(s))
