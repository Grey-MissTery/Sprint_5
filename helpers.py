import random
import string

def generate_email_correct():
    domains = ["gmail.com", "yandex.ru", "mail.ru"]
    return f"test_user_{random.randint(1, 100000000000)}@{random.choice(domains)}"

def generate_email_invalid():
    domains = ["gmail.com", "yandex.ru", "mail.ru"]
    return f"test_user_{random.randint(1, 100000000000)}{random.choice(domains)}"

def generate_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(12))

def generate_title():
    random_part = ''.join(random.choice(string.ascii_letters) for i in range(10))
    return f"Test {random_part}"

def generate_description():
    random_part = ''.join(random.choice(string.ascii_letters + string.digits + " ") for i in range(50))
    return f"Test {random_part}"

def generate_price():
    return random.randint(1, 1000000)
