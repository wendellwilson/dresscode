from dress.errors import DressingError
from dress.aoc import AoC
from dress.constants import SOCKS, PANTS, SHOES, SHIRT, HAT, LEAVE, \
    OUTPUT_DEL, FAILURE_MESSAGE, OPTION_NAMES

RESTRICTED_ERROR_MESSAGE = ""

class Worker(object):

    def __init__(self, name):
        self.name = name
        self.worn = []
        self.state = ""
        socks = AoC(OPTION_NAMES[SOCKS], SOCKS, True)
        pants = AoC(OPTION_NAMES[PANTS], PANTS, True)
        shoes = AoC(OPTION_NAMES[SHOES], SHOES, True, {socks, pants})
        shirt = AoC(OPTION_NAMES[SHIRT], SHIRT, True)
        hat = AoC(OPTION_NAMES[HAT], HAT, False, {shirt})
        self.my_clothes = [socks, pants, shoes, shirt, hat]

    def get_dressed(self, order):
        if not self.state:
            clothes = []
            for code in order:
                if code == LEAVE:
                    break
                else:
                    clothes.append(self._get_aoc_by_code(code))
            try:
                self._dress(clothes)
                self._leave()
            except DressingError:
                self._fail()

    def _dress(self, clothes):
        # put on an item of clothing, fail or leave
        for item in clothes:
            self._wear(item)

    def _leave(self):
        # leave if fully dressed
        if self._get_essential_aoc().issubset(set(self.worn)):
            self.state = OPTION_NAMES[LEAVE]
        else:
            raise DressingError("leave")

    def _fail(self):
        self.state = FAILURE_MESSAGE

    def _wear(self, item):
        if item.get_req().issubset(set(self.worn)):
            self.worn.append(item)
        else:
            raise DressingError("wear")

    def _get_aoc_by_code(self, code):
        return next(filter(lambda x: x.get_code() == code,  self.my_clothes))

    def _get_essential_aoc(self):
        return set(filter(lambda x: x.is_essential() is True,  self.my_clothes))

    def __str__(self):
        wearing = OUTPUT_DEL.join(map(str, self.worn))
        if self.state:
            return '%s%s%s'  % (wearing, OUTPUT_DEL, self.state)
        return wearing
