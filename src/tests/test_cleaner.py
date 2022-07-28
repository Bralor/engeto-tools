import xml.etree.ElementTree as te
import task_manager.cleaner as tc


def test_if_select_names_returns_expected_result():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercise = [exe for exe in root.iter("exercise")]
    assert tc.select_names(exercise, {"L01": "lesson01"}) == {'unit_converter'}


def test_if_write_description_returns_expected_data_type():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercise = [exe for exe in root.iter("exercise")]
    result = tc.select_names(exercise, {"L01": "lesson01"})
    assert isinstance(result, set)
