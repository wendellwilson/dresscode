# Article of Clothing
class AoC():
    def __init__(self, name, code, essential, prereq):
        self.name = name
        self.code = code
        self.essential = essential
        self.prereq = prereq

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def get_req(self):
        return self.req

    def is_essential(self):
        return self.essential

    def set_prereq(self, prereq):
        self.prereq = prereq

    def __str__(self):
        return self.name