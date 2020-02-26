class InputError(Exception):
    """Exception raised for errors in the input.
    """

    def __init__(self, user_input):
        self.user_input = user_input


class DressingError(Exception):
    """Raised when a failure in worker dressing occurs
    """

    def __init__(self, fail_step):
        self.fail_step = fail_step
