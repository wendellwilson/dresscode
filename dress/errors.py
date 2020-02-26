class DressingError(Exception):
    '''Raised when a failure in worker dressing occurs
    '''

    def __init__(self, fail_step):
        self.fail_step = fail_step
