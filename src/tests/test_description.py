import pytest

import src.task_manager.description as td


exerc_1 = (
        'slicing_string', {
             'folder': 'exercises',
             'lesson': 'L01',
             'path': 'exercises/L01/slicing_string/solution'
         }
)
exerc_2 = (
        'slicing_string', {
             'folder': 'exercises',
             'path': 'exercises/L01/slicing_string/solution'
         }
)


@pytest.mark.parametrize("data, result",
        [
            (exerc_1, "lesson01"),
            (exerc_2, "nan_lesson")
        ]
)
def test_if_data_contains_key_lesson(data: tuple, result: str):
    lessons = {"L01": "lesson01"}
    assert td.get_current_lesson(data, lessons) == result



