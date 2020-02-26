import pytest
from dress.worker import Worker


@pytest.mark.parametrize(
    "order, output",
    [
        ([5, 1], "socks, fail"),  # hat no shirt
        ([2, 4, 5, 3], "pants, fail"),  # shoes no sock
        ([5, 4, 2], "socks, fail"),  # shoes no pants
        ([2, 5, 4], "pants, socks, shoes, fail"), # no shirt leave
        ([3, 1, 5, 2, 6], "shirt, hat, socks, pants, fail"), # no shoes leave
        ([5, 2, 3, 4, 6], "socks, pants, shirt, shoes, leave"),  # no hat leave
        ([3, 2, 5, 4, 1], "shirt, pants, socks, shoes, hat, leave"), # everything leave
        ([5, 2, 3, 6, 4], "socks, pants, shirt, fail"),  # leave early
    ],
)
def test_get_dressed(order, output):
    worker = Worker("Sam")
    worker.get_dressed(order)
    assert str(worker) == output
