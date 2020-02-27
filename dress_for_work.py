from dress.constants import INPUT_ERROR_MESSAGE, INPUT_PROMPT
from dress.worker import Worker
from dress.utils import clean_input


print(INPUT_PROMPT)
# loop until we get a good user input
while True:
    try:
        user_input = input()
        cleaned_input = clean_input(user_input)
        break
    except ValueError:
        print(INPUT_ERROR_MESSAGE)

# create worker
wendell = Worker("Wendell")
# give worker dressing orders
wendell.get_dressed(cleaned_input)
# print worker
print(str(wendell))

