import random

import name_list
import config


def generate_numbers(numbers_count=random.randint(1, config.max_end_numbers_count)) -> str:
    """ Generate random number """

    return_text = ""

    for i in range(numbers_count):
        return_text += str(random.randint(0, 9))  # Generate random number
    if config.end_numbers_year:
        return_text = str(random.randint(config.end_numbers_year_range[0], config.end_numbers_year_range[1]))

    return return_text


def generate_name(end_numbers: bool = True) -> str:
    """ Generate random name """

    first_name = random.choice(name_list.get_words_from_file(config.first_name_file)).title()  # Generate first name
    last_name = random.choice(name_list.get_words_from_file(config.last_name_file)).title()  # Generate last name

    name = first_name + last_name

    if end_numbers:
        name += generate_numbers()  # Add random numbers
    return name


if __name__ == "__main__":
    print(generate_name())
