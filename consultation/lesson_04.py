def contains_digit(value):
    return (
        "0" in value or
        "1" in value or
        "2" in value or
        "3" in value or
        "4" in value or
        "5" in value or
        "6" in value or
        "7" in value or
        "8" in value or
        "9" in value
    )

is_it_digit = contains_digit("I'm 111 years old")
print(is_it_digit)