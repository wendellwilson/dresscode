# instruction options
HAT = 1
PANTS = 2
SHIRT = 3
SHOES = 4
SOCKS = 5
LEAVE = 6

# associated output of instructions
OPTION_NAMES= {
    HAT: "hat",
    PANTS: "pants",
    SHIRT: "shirt",
    SHOES: "shoes",
    SOCKS: "socks",
    LEAVE: "leave",
}
FAILURE_MESSAGE = "fail"

# delimiters
INPUT_DEL = ' '
OUTPUT_DEL = ', '

# messages
INPUT_INSTRUCTIONS = "Please input a space separated list of numbers to indicate articles of " \
                "clothing or actions."
INPUT_ERROR_INTRO = "Invalid input."
OPTION_KEY = ', '.join("{!s}={!r}".format(key, val) for (key, val) in OPTION_NAMES.items())
INPUT_ERROR_MESSAGE = "%s %s %s" % (INPUT_ERROR_INTRO, INPUT_INSTRUCTIONS , OPTION_KEY)
INPUT_PROMPT = "%s %s" % (INPUT_INSTRUCTIONS , OPTION_KEY)
