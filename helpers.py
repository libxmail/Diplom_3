import random


def generate_email():
    random_digits = random.randint(1000, 9999)
    return f"sergei_fedotov_53_{random_digits}@yandex.ru"


def generate_password():
    return str(random.randint(100000, 999999))
