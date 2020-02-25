import pytest
import dress_for_work as dfw

@pytest.mark.parametrize(
    "order, output",
    [
        ("5 1", "socks, fail"),  # hat no shirt
        ("2 4 5 3", "pants, fail"),  # shoes no sock
        ("5 4 2", "socks, fail"),  # shoes no pants
        ("2 5 4", "pants, socks, shoes, fail"), # no shirt leave
        ("3 1 5 2 6", "shirt, hat, socks, pants, fail"), # no shoes leave
        ("5 2 3 4 6", "socks, pants, shirt, shoes, leave"),  # no hat leave
        ("3 2 5 4 1", "shirt, pants, socks, shoes, hat, leave"), # everything leave
    ],
)
def test_get_dressed(order, output):
    assert dfw.get_dressed(input) == output

@pytest.mark.parametrize(
    "input",
    [
        "5e4",
        "5 2 3 4 7",
        "",
    ],
)
def test_clean_input(input):
    with pytest.raises(ValueError):
        dfw.clean_input(input)
