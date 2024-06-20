import random as rd


# Function that generate lists of characters and shuffle them for randomness
def chars_lists():
    low_letters_list = [chr(letter) for letter in range(97, 123)]
    rd.shuffle(low_letters_list)

    nums_list = [num for num in range(10)]
    rd.shuffle(nums_list)

    cap_letters_list = [chr(letter) for letter in range(65, 91)]
    rd.shuffle(cap_letters_list)

    special_char_str = """'~`!@#$%^&*()_-+={[}]|:;"'<,>.?/"""
    special_chars_list = [char for char in special_char_str]
    rd.shuffle(special_chars_list)

    return low_letters_list, nums_list, cap_letters_list, special_chars_list


lower_letters, numbers, cap_letters, special_char = chars_lists()


def passwd_generator(lower_letters_quantity, numbers_quantity, cap_letters_quantity, special_char_quantity):

    # Choose random characters based on specified quantities
    chosen_lower_letters = rd.choices(lower_letters, k=lower_letters_quantity)
    chosen_numbers = rd.choices(numbers, k=numbers_quantity)
    chosen_cap_letters = rd.choices(cap_letters, k=cap_letters_quantity)
    chosen_special_char = rd.choices(special_char, k=special_char_quantity)

    # Combine and shuffle all chosen characters to form the password
    passwd_list = chosen_lower_letters + chosen_numbers + chosen_cap_letters + chosen_special_char
    rd.shuffle(passwd_list)
    passwd = ''.join(str(x) for x in passwd_list)

    return passwd


# Function to generate a default password with random characteristics
def default_passwd():
    length = rd.randint(16, 25)
    lower_letters_quantity = rd.randint(5, (length - 2*4 - 3))
    numbers_quantity = rd.randint(4, (length - lower_letters_quantity - 3 - 4))
    cap_letters_quantity = rd.randint(3, (length - lower_letters_quantity - numbers_quantity - 4))
    special_char_quantity = rd.randint(4, (length - lower_letters_quantity - numbers_quantity - cap_letters_quantity))

    return passwd_generator(lower_letters_quantity, numbers_quantity, cap_letters_quantity, special_char_quantity)


# Dictionary that used to Trigger if the user didn't input anything then the func. will generate default passwd
default_dict = {
    'lower_letters': 0,
    'numbers': 0,
    'cap_letters': 0,
    'special_char': 0
}


# Function to generate a custom password based on specified requirements
def custom_passwd(values_dict=default_dict):
    # If no custom values provided, generate a default password
    if values_dict == default_dict:
        return default_passwd()

    # Extract values from the input dictionary to customize the password
    for key in values_dict.keys():
        match key:
            case 'lower_letters':
                lower_letters_quantity = values_dict.get(key)
            case 'numbers':
                numbers_quantity = values_dict.get(key)
            case 'cap_letters':
                cap_letters_quantity = values_dict.get(key)
            case 'special_char':
                special_char_quantity = values_dict.get(key)

    return passwd_generator(lower_letters_quantity, numbers_quantity, cap_letters_quantity, special_char_quantity)


if __name__ == '__main__':
    test_dict = {
        'lower_letters': 5,
        'numbers': 4,
        'cap_letters': 4,
        'special_char': 3
    }

    print(custom_passwd(test_dict))
