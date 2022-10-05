import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, human_age", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_human_age_in_cat_dog_age(cat_age: int,
                                  dog_age: int,
                                  human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
