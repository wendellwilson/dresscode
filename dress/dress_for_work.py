from errors import InputError
from constants import INPUT_DEL, OPTION_NAMES, INPUT_ERROR_MESSAGE


def clean_input(self, user_input):
    try:
        input_list = str.split(user_input, INPUT_DEL)
        final_input = []
        for item in input_list:
            # make sure numbers are valid inputs
            if int(item) not in OPTION_NAMES.keys():
                raise InputError(user_input)
            # remove duplicate items of clothing
            else:
                if item not in final_input:
                    final_input.append(item)
    except InputError:
        print(INPUT_ERROR_MESSAGE)
