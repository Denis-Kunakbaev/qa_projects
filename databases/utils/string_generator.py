import random, string


class RandomTextGenerator:
    @staticmethod
    def get_random_text(message_length):
        return ''.join(random.choices(string.ascii_letters, k=message_length))