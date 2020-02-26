


def clean_input(self, user_input):
    try:
        input_list = str.split(user_input, INPUT_DEL)
        final_input = []
        for item in input_list:
            # make sure numbers are valid inputs
            if int(item) not in self.ALL_INPUTS:
                raise ValueError
            # remove duplicate items of clothing
            else:
                if item not in final_input:
                    final_input.append(item)
    except ValueError:
        print(ERROR_MESSAGE)
