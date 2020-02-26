# Article of Clothing
class AoC(object):
    def __init__(self, name, code, essential, req=set()):
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
