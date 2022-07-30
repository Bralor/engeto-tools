import xml.etree.ElementTree as te
import task_manager.tasknames as ttn


def test_get_all_tasks_returns_expected_result_len():
    test_xml = "./exercise.xml"
    tree = te.parse(test_xml)
    root = tree.getroot()
    assert len(ttn.get_all_tasks(root, 'exercise')) == 1

def test_get_all_tasks_returns_expected_data_type():
    test_xml = "./exercise.xml"
    tree = te.parse(test_xml)
    root = tree.getroot()
    result = ttn.get_all_tasks(root, 'exercise')
    assert isinstance(result, list)


def test_get_specific_elements_returns_expected_result_len():
    test_xml = "./exercise.xml"
    tree = te.parse(test_xml)
    root = tree.getroot()
    assert len(ttn.get_specific_elements(root, "exercise", "name", "P")) == 1


def test_get_specific_elements_returns_expected_data_type():
    test_xml = "./exercise.xml"
    tree = te.parse(test_xml)
    root = tree.getroot()
    result = ttn.get_specific_elements(root, "exercise", "name", "P")
    assert isinstance(result, list)


def test_test_select_attr_value_returns_expected_data_type_returns_expected_result():
    tree = te.parse("./exercise.xml")
    root = tree.getroot()
    elms = [
        element
        for element in root.iter("exercise")
        if element.get("name").startswith("P")
    ]
    assert len(ttn.select_attr_value(elms, "name")) == 1


def test_select_attr_value_returns_expected_data_type():
    test_xml = "./exercise.xml"
    tree = te.parse(test_xml)
    root = tree.getroot()
    elms = [
        element
        for element in root.iter("exercise")
        if element.get("name").startswith("P")
    ]
    result = ttn.select_attr_value(elms, "name")
    assert isinstance(result, list)


def test_get_task_names_returns_expected_result():
    test_xml = "./exercise.xml"
    tree = te.parse(test_xml)
    root = tree.getroot()
    assert ttn.get_task_names(root, "exercise", "name", "P", "name") == ['Převaděč jednotek']


def test_get_task_names_returns_expected_data_type():
    test_xml = "./exercise.xml"
    tree = te.parse(test_xml)
    root = tree.getroot()
    result = ttn.get_task_names(root, "exercise", "name", "P", "name")
    assert isinstance(result, list)


def test_create_task_data_returns_expected_result():
    assert ttn.create_task_data(("hhh/kkk/sss/ddd",)) == {'sss': {'folder': 'hhh', 'lesson': 'kkk', 'path': 'hhh/kkk/sss/ddd'}}


def test_create_task_data_returns_expected_data_type():
    result = ttn.create_task_data(("hhh/kkk/sss/ddd",))
    assert isinstance(result, dict)


def test_parse_name_returns_expected_result():
    assert ttn.parse_name("foo/bar/fii/doo") == ('foo', 'bar', 'fii')


def test_parse_name_returns_expected_data_type():
    result = ttn.parse_name("foo/bar/fii/doo")
    assert isinstance(result, tuple)


def test_get_only_task_name_expected_result():
    assert ttn.get_only_task_name( {"task1":
             {"folder": "a", "lesson": "L01", "path": "foo"},
         "task2":
             {"folder": "b", "lesson":"L02", "path": "bar"}
         }) == ('task1', 'task2')


def test_get_only_task_name_expected_data_type():
    result = ttn.get_only_task_name( {"task1":
             {"folder": "a", "lesson": "L01", "path": "foo"},
         "task2":
             {"folder": "b", "lesson":"L02", "path": "bar"}
         })
    assert isinstance(result, tuple)