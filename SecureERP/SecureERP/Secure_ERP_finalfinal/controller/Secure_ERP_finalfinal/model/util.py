import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    myId = []
    for small_letter in range(number_of_small_letters):
        myId.append(random.choice(string.ascii_lowercase))
    for capital_letter in range(number_of_capital_letters):
        myId.append(random.choice(string.ascii_uppercase))
    for digit in range(number_of_digits):
        myId.append(str(random.randint(1, 10)))
    for special_char in range(number_of_special_chars):
        myId.append(random.choice(allowed_special_chars))
    random.shuffle(myId)
    return ''.join(myId)
