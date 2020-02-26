HAT = 1
PANTS = 2
SHIRT = 3
SHOES = 4
SOCKS = 5
LEAVE = 6

OPTION_NAMES= {
    HAT: "hat",
    PANTS: "pants",
    SHIRT: "shirt",
    SHOES: "shoes",
    SOCKS: "socks",
    LEAVE: "leave",
}

INPUT_DEL = ' '
OUTPUT_DEL = ', '

FAILURE_MESSAGE = "fail"

INPUT_ERROR_INTRO = "Invalid input. Please input a space separated list of numbers to indicate articles of " \
                "clothing or actions."
OPTION_KEY = ', '.join("{!s}={!r}".format(key, val) for (key, val) in OPTION_NAMES.items())
INPUT_ERROR_MESSAGE = "%s %s" % (INPUT_ERROR_INTRO, OPTION_KEY)

