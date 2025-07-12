import pytest

from pr_tutorial.buggy_function import angle_to_sexigesimal


@pytest.mark.parametrize(
    "angle, expected",
    [
        (0, "0:0:0"),
        (90, "3:0:0"),
        (30, "1:0:0"),
        (45, "1:30:0"),
        (60, "2:0:0"),
    ],
)
def test__angle_to_sexigesimal(angle: float, expected: str):
    assert angle_to_sexigesimal(angle) == expected
