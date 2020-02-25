

class DressForWork(object):
    #clothing items
    HAT = 1
    PANTS = 2
    SHIRT = 3
    SHOES = 4
    SOCKS = 5
    #actions
    LEAVE = 6

    ITEMS = {
        HAT: "hat",
        PANTS: "pants",
        SHIRT: "shirt",
        SHOES: "shoes",
        SOCKS: "socks",
    }

    #clothing limitations
    SHOES_REQ = [PANTS, SOCKS]
    HAT_REQ = [SHIRT]
    LEAVE_REQ  = [SHIRT, SHOES, SOCKS, PANTS]

    FAILURE_MESSAGE = "fail"
    LEAVE_MESSAGE = "leave"

    #delimiters
    INPUT_DEL = ' '
    OUTPUT_DEL = ','

    def get_dressed(self, input): ... #do everything to get dressed and output pretty

    def dress(self, order): ... #get dressed return list of actions

    def clean_input(self, input): ... #validate and return list or throw error