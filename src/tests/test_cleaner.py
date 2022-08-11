import xml.etree.ElementTree as te
import task_manager.cleaner as tc


def test_if_select_names_returns_expected_result():
    tree = te.parse("src/tests/exercise.xml")
    root = tree.getroot()
    exercise = [exe for exe in root.iter("exercise")]
    assert tc.select_names(exercise) == {'unit_converter'}


def test_if_select_names_returns_expected_data_type():
    tree = te.parse("src/tests/exercise.xml")
    root = tree.getroot()
    exercise = [exe for exe in root.iter("exercise")]
    result = tc.select_names(exercise)
    assert isinstance(result, set)
