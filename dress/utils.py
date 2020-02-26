from dress.constants import INPUT_DEL, OPTION_NAMES


def clean_input(dirty_input):
    '''
    checkes that a input is valid and converts it into a list of clothing options
    :param dirty_input: user input to be cleaned
    :return: list of numbers that corespond to available options constants.OPTION_NAMES
    '''
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
