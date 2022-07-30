import xml.etree.ElementTree as te
import task_manager.cleaner as tc


def test_select_names_returns_expected_result():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exe for exe in root.iter("exercise")]
    assert tc.select_names(exercises) == {'unit_converter'}


def test_select_names_returns_expected_data_type():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exe for exe in root.iter("exercise")]
    result = tc.select_names(exercises)
    assert isinstance(result, set)


def test_select_attr_returns_expected_result():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exe for exe in root.iter("exercise")]
    assert tc.select_attr(exercises[0], "solution", "sourceDir") == 'exercises/L01/unit_converter/solution'


def test_select_attr_returns_expected_data_type():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exe for exe in root.iter("exercise")]
    result = tc.select_attr(exercises[0], "solution", "sourceDir")
    assert isinstance(result, str)


def test_split_name_returns_expected_result():
    assert tc.split_name("engeto-tools/src/task_manager/attributes") == 'task_manager'


def test_split_name_returns_expected_data_type():
    result = tc.split_name("engeto-tools/src/task_manager/attributes")
    assert isinstance(result, str)


def test_split_name_returns_expected_result():
    assert tc.split_name("engeto-tools/src/task_manager/attributes") == 'task_manager'
