from dress.aoc import AoC
from dress.constants import SOCKS, PANTS, SHOES, SHIRT, HAT, LEAVE, \
    OUTPUT_DEL, FAILURE_MESSAGE, LEAVE_MESSAGE, CLOTHING_NAMES



class Worker(object):

    def __init__(self, name):
        self.name = name
        self.worn = []
        state = ""
        socks = AoC(CLOTHING_NAMES[SOCKS], SOCKS, True)
        pants = AoC(CLOTHING_NAMES[PANTS], PANTS, True)
        shoes = AoC(CLOTHING_NAMES[SHOES], SHOES, True, {socks, pants})
        shirt = AoC(CLOTHING_NAMES[SHIRT], SHIRT, True)
        hat = AoC(CLOTHING_NAMES[HAT], HAT, False, {shirt})
        self.my_clothes = [socks, pants, shoes, shirt, hat]

    def get_dressed(self, order):
        clothes = []
        for code in order:
            if code == LEAVE:
                break
            else:
                clothes.append(self._get_aoc_by_code(code))
        try:
            self._dress(clothes)
            self._leave()
        except DressingException:
            self._fail()

    def _dress(self, clothes):
        # put on an item of clothing, fail or leave
        for item in clothes:
            self._wear(item)

    def _leave(self):
        # leave if fully dressed
        if self._get_essential_aoc().issubset(set(self.worn)):
            self.state = LEAVE_MESSAGE
        else:
            return self._fail()

    def _fail(self):
        self.state = FAILURE_MESSAGE

    def _wear(self, item):
        if item.get_req().issubset(set(self.worn)):
            self.worn.append(item)
        else:
            self._fail()

    def _get_aoc_by_code(self, code):
        return next(filter(lambda x: x.get_code() == code,  self.myclothes))

    def _get_essential_aoc(self):
        return set(filter(lambda x: x.is_essential() is True,  self.myclothes))

    def __str__(self):
        wearing = OUTPUT_DEL.join(self.my_clothes)
        if self.state:
            return '%s%s%s'  % (wearing, OUTPUT_DEL, self.state)
        return wearing
