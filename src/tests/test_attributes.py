import xml.etree.ElementTree as te

import task_manager.attributes as ta


def test_update_exercise_with_proper_elements():
    tree = te.parse('src/tests/exercise.xml')
    root = tree.getroot()
    out = {
        'Převaděč jednotek':
        {
            'perex': 'nan_sourceDir',
            'exercise-folder': 'exercises/L01/unit_converter/exercise-folder',
            'unit-tests': 'nan_sourceDir',
            'solution': 'exercises/L01/unit_converter/solution',
            'description': 'exercises/L01/unit_converter/exercise-folder'
        }
    }
    exercises = [exercise for exercise in root.iter('exercise')]
    ta.update_exercise(
        exercises[0], out[exercises[0].attrib['name']],
        'sourceDir', 'exercise-folder', 'unit-tests'
    )
    assert exercises[0].find(
        'tests'
    ).attrib['srcTests'] == 'exercises/L01/unit_converter/tests.py'


def test_update_attribute_returns_expected_result():
    tree = te.parse('src/tests/exercise.xml')
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter('exercise')]
    assert ta.update_attribute(
        exercises[0].find(
            'tests'
        ), 'srcTests', 'exercises/L01/unit_converter/tests.py'
    ) == 'exercises/L01/unit_converter/tests.py'


def test_if_update_attribute_returns_expected_data_type():
    tree = te.parse('src/tests/exercise.xml')
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter('exercise')]
    result = ta.update_attribute(
        exercises[0].find('solution'),
        'sourceDir', 'exercises/L01/unit_converter/solution'
    )
    assert isinstance(result, str)


def test_collect_data_returns_expected_result():
    tree = te.parse('src/tests/exercise.xml')
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter('exercise')]
    assert ta.collect_data(
        exercises
    ) == {
        'Převaděč jednotek':
        {
            'perex': 'nan_sourceDir',
            'exercise-folder': 'exercises/L01/unit_converter/exercise-folder',
            'tests': 'nan_sourceDir',
            'description': 'exercises/L01/unit_converter/exercise-folder',
            'solution': 'exercises/L01/unit_converter/solution'
        }
    }


def test_if_collect_data_returns_expected_data_type():
    tree = te.parse('src/tests/exercise.xml')
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter('exercise')]
    result = ta.collect_data(exercises)
    assert isinstance(result, dict)


def test_collect_task_data_returns_expected_result():
    tree = te.parse('src/tests/exercise.xml')
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter('exercise')]
    out = ta.collect_task_data(exercises[0])
    assert out[
        'exercise-folder'
    ] == 'exercises/L01/unit_converter/exercise-folder'


def test_if_collect_task_data_returns_expected_data_type():
    tree = te.parse('src/tests/exercise.xml')
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter('exercise')]
    out = ta.collect_task_data(exercises[0])
    assert isinstance(out, dict)


def test_replace_values_returns_expected_result():
    out = {
        'Převaděč jednotek':
        {
            'perex': 'nan_sourceDir',
            'exercise-folder': 'exercises/L01/unit_converter/exercise-folder',
            'unit-tests': 'nan_sourceDir',
            'solution': 'exercises/L01/unit_converter/solution',
            'description': 'exercises/L01/unit_converter/exercise-folder'
        }
    }
    assert ta.replace_values(
        out)['Převaděč jednotek']['perex'] == 'nan_sourceDir'


def test_if_replace_values_returns_expected_data_type():
    out = {
        'Převaděč jednotek':
        {
            'perex': 'nan_sourceDir',
            'exercise-folder': 'exercises/L01/unit_converter/exercise-folder',
            'unit-tests': 'nan_sourceDir',
            'solution': 'exercises/L01/unit_converter/solution',
            'description': 'exercises/L01/unit_converter/exercise-folder'
        }
    }
    result = ta.replace_values(out)
    assert isinstance(result, dict)
