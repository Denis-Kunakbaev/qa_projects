import random


class IdGenerator:
    @staticmethod
    def generate_random_id_with_repeating_digits(limit=10):
        ids = []
        for _ in range(limit):
            digit = str(random.randint(1, 9))
            ids.append(int(digit * 2))
        return ids

    @staticmethod
    def generate_random_id_for_project(projects_count):
        id = random.randint(1, projects_count)
        return id
