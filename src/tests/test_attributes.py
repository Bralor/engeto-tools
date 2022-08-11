import xml.etree.ElementTree as te

import task_manager.attributes as ta

from task_manager.utils import lesson01


def test_update_exercise_with_proper_elements():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    out = {
        'Převaděč jednotek':
        {
            'perex': 'nan_sourceDir',
            'skeleton': 'exercises/L01/unit_converter/skeleton',
            'unit-tests': 'nan_sourceDir',
            'solution': 'exercises/L01/unit_converter/solution',
            'description': 'exercises/L01/unit_converter/skeleton'
        }
    }
    exercises = [exercise for exercise in root.iter("exercise")]
    ta.update_exercise(
        exercises[0], out[exercises[0].attrib["name"]],
        "sourceDir", "skeleton", "unit-tests"
    )
    assert exercises[0].find(
        "skeleton"
    ).attrib["sourceDir"] == "exercises/L01/unit_converter/skeleton"


def test_update_attribute_returns_expected_result():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter("exercise")]
    assert ta.update_attribute(
        exercises[0].find(
            "skeleton"
        ), "sourceDir", "exercises/L01/unit_converter/skeleton"
    ) == 'exercises/L01/unit_converter/skeleton'


def test_if_update_attribute_returns_expected_data_type():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter("exercise")]
    result = ta.update_attribute(
        exercises[0].find("skeleton"),
        "sourceDir", "exercises/L01/unit_converter/skeleton"
    )
    assert isinstance(result, str)


def test_collect_data_returns_expected_result():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter("exercise")]
    assert ta.collect_data(exercises) == {
        'Převaděč jednotek':
        {
            'perex': 'nan_sourceDir',
            'skeleton': 'exercises/L01/unit_converter/skeleton',
            'unit-tests': 'exercises/L01/unit_converter/tests.py',
            'description': 'exercises/L01/unit_converter/skeleton',
            'solution': 'exercises/L01/unit_converter/solution'
        }
    }


def test_if_collect_data_returns_expected_data_type():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter("exercise")]
    result = ta.collect_data(exercises)
    assert isinstance(result, dict)


def test_collect_task_data_returns_expected_result():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter("exercise")]
    out = ta.collect_task_data(exercises[0])
    assert out['skeleton'] == 'exercises/L01/unit_converter/skeleton'


def test_if_collect_task_data_returns_expected_data_type():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter("exercise")]
    out = ta.collect_task_data(exercises[0])
    assert isinstance(out, dict)


def test_replace_values_returns_expected_result():
    out = {
        'Převaděč jednotek':
        {
            'perex': 'nan_sourceDir',
            'skeleton': 'exercises/L01/unit_converter/skeleton',
            'unit-tests': 'nan_sourceDir',
            'solution': 'exercises/L01/unit_converter/solution',
            'description': 'exercises/L01/unit_converter/skeleton'
        }
    }
    assert ta.replace_values(
        out, lesson01)['Převaděč jednotek']['perex'] == 'nan_sourceDir'


def test_if_replace_values_returns_expected_data_type():
    out = {
        'Převaděč jednotek':
        {
            'perex': 'nan_sourceDir',
            'skeleton': 'exercises/L01/unit_converter/skeleton',
            'unit-tests': 'nan_sourceDir',
            'solution': 'exercises/L01/unit_converter/solution',
            'description': 'exercises/L01/unit_converter/skeleton'
        }
    }
    result = ta.replace_values(out, lesson01)
    assert isinstance(result, dict)
