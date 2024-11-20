import re


class StringFormatter:
    @staticmethod
    def __normalize_slashes(string):
        return re.sub(r'\\+', r'\\', string)

    @staticmethod
    def __remove_escaped_apostrophes(string):
        return re.sub(r"\\'", "'", string)

    @staticmethod
    def __normalize_spaces(string):
        return re.sub(r'\s+', ' ', string)

    @staticmethod
    def __replace_double_quotes(string):
        return string.replace('"', "'")

    @staticmethod
    def format_string_from_web(string):
        normalized = StringFormatter.__normalize_slashes(string)
        normalized = StringFormatter.__remove_escaped_apostrophes(normalized)
        normalized = StringFormatter.__normalize_spaces(normalized)
        normalized = StringFormatter.__replace_double_quotes(normalized)
        return normalized

    @staticmethod
    def format_string_from_api(string):
        normalized = StringFormatter.__normalize_spaces(string)
        normalized = StringFormatter.__replace_double_quotes(normalized)
        return normalized
