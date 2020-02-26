from dress.constants import INPUT_DEL, OPTION_NAMES


def clean_input(dirty_input):
    input_list = str.split(dirty_input, INPUT_DEL)
    final_input = []
    for item in input_list:
        item = int(item)
        # make sure numbers are valid inputs
        if item not in OPTION_NAMES.keys():
            raise ValueError
        # remove duplicate items of clothing
        else:
            if item not in final_input:
                final_input.append(item)
    return final_input
