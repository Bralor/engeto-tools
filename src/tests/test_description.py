import pytest
import xml.etree.ElementTree as te

import task_manager.description as td


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
             'path': 'exercises/L01/slicing_strig/solution'
         }
)


@pytest.mark.parametrize("data, result",
        [
            (exerc_1, "lesson01"),
            (exerc_2, "nan_lesson")
        ]
)


def test_data_contains_key_lesson(data: tuple, result: str):
    lessons = {"L01": "lesson01"}
    assert td.get_current_lesson(data, lessons) == result




def test_repo_contains_task_name():
    pattern = {"slicing_string": "rozdeleni_stringu"}
    assert td.get_current_name("slicing_string", pattern) == 'rozdeleni_stringu'


def test_get_current_name_returns_expected_data_type():
    pattern = {"slicing_string": "rozdeleni_stringu"}
    result = td.get_current_name("slicing_string", pattern)
    assert isinstance(result, str)


def test_read_description_returns_expected_result_len():
    result = td.read_description('../engeto_tasks', 'rozdeleni_stringu', 'lesson01')
    assert len(result) > 0


def test_read_description_returns_expected_data_type():
    result = td.read_description('../engeto_tasks', 'rozdeleni_stringu', 'lesson01')
    assert isinstance(result, list)


def test_write_description_returns_expected_result():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exe for exe in root.iter("exercise")]
    assert td.write_description('test text', exercises[0], 'perex') == 'test text'


def test_write_description_returns_expected_data_type():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exe for exe in root.iter("exercise")]
    result = td.write_description('test text', exercises[0], 'perex')
    assert isinstance(result, str)
