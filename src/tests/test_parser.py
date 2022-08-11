import xml.etree.ElementTree as te
import task_manager.parser as tp


def test_if_get_xml_root_returns_expected_data_type():
    assert isinstance(tp.get_xml_root("./exercise.xml"), te.ElementTree)


def test_if_set_xml_attr_returns_expected_result():
    assert tp.set_xml_attr(
        name="Destinatio 1", lesson='L01'
    ) == {'name': 'Destinatio 1', 'lesson': 'L01'}


def test_if_set_xml_attr_expected_data_type():
    assert isinstance(tp.set_xml_attr(name="Destinatio 1", lesson='L01'), dict)
