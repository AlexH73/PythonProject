import re

def greeting(str):
    print(f"Hello {str}!")


def is_valid_email(email):
    # [a-zA-Z0-9.-_]@[a-zA-Z0-9].[a-z]
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        print(f"{email} is valid")
    else:
        print(f"{email} is not valid")

greeting("Alexander")
is_valid_email("asdfgfdsd@sda.re")
greeting("Alex")
is_valid_email("asdfgfdsd@sdare")