# Article of Clothing
class AoC(object):
    """Article of Clothing

        name - name of the clothing
        code - integer code used to refer to the clothing
        essential - if this clothing is required to leave the house
        req - other clothing required to be worn before this clothing
    """
    def __init__(self, name, code, essential, req=None):
        if req is None:
            req = set()
        self.name = name
        self.code = code
        self.essential = essential
        self.req = req

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def is_essential(self):
        return self.essential

    def get_req(self):
        return self.req

    def set_req(self, req):
        self.req = req

    def __str__(self):
        return self.name
