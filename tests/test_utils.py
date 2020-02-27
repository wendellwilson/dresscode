import pytest
from dress.utils import clean_input

@pytest.mark.parametrize(
    "user_input, cleaned_input",
    [
        ("5 1", [5, 1]),
        ("5 1 1", [5, 1]),  # duplicates
        ("5 2 3 6 4", [5, 2, 3, 6, 4]),
    ],
)
def test_get_dressed(user_input, cleaned_input):
    assert clean_input(user_input) == cleaned_input


@pytest.mark.parametrize(
    "user_input",
    [
        "5e4",
        "5 2 3 4 7",
        "",
    ],
)
def test_clean_input_error(user_input):
    with pytest.raises(ValueError):
        clean_input(user_input)
