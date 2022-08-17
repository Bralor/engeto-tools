import xml.etree.ElementTree
from typing import List, Union, Dict, Tuple, Optional


def get_all_tasks(
    root: xml.etree.ElementTree.Element, value: str
) -> List[xml.etree.ElementTree.Element]:
    """
    Return the list of all XML tags that have specific names.

    :param root: an object with the content of the XML file.
    :type root: xml.etree.ElementTree.Element
    :param value: a name of the searched element.
    :type value: str
    :return: a list of specific elements.
    :rtype: list

    :Example:
    >>> import xml.etree.ElementTree
    >>> test_xml = "src/tests/foo.xml"
    >>> tree = xml.etree.ElementTree.parse(test_xml)
    >>> root = tree.getroot()
    >>> len(get_all_tasks(root, "country"))
    3
    """
    return [
        exercise
        for exercise in root.iter(value)
    ]


def get_specific_elements(
        root: xml.etree.ElementTree.Element,
        xml_tag: str, xml_attr: str, attr_val: str
) -> List[xml.etree.ElementTree.Element]:
    """
    From the given root, return the list of elements that are matching given
    keyword arguments.

    :param root: an object with the content of the XML file.
    :type root: xml.etree.ElementTree.Element
    :param params: a dictionary with specific xml attributes.
    :type params: dict
    :return: a list of specific elements.
    :rtype: list

    :Example:
    >>> import xml.etree.ElementTree as xml
    >>> tree = xml.parse("src/tests/foo.xml")
    >>> root = tree.getroot()
    >>> len(get_specific_elements(root, "country", "name", "P"))
    1
    """
    return [
        element
        for element in root.iter(xml_tag)
        if element.get(xml_attr).startswith(attr_val)  # type: ignore
    ]


def select_attr_value(
    elements: List[xml.etree.ElementTree.Element],
    attr_name: str
) -> List[Union[str, None]]:
    """
    From the given list of elements, get the list of names.

    :param elements: an object of elements (from the XML root).
    :type elements: list
    :param attr_name: a name of the XML attribute.
    :type attr_name: str
    :return: a list of all searched attribute values.
    :rtype: list

    :Example:
    >>> import xml.etree.ElementTree as xml
    >>> tree = xml.parse("src/tests/foo.xml")
    >>> root = tree.getroot()
    >>> elms = [
    ...    element
    ...    for element in root.iter("country")
    ...    if element.get("name").startswith("P")
    ... ]
    >>> rank = select_attr_value(elms, "name")
    >>> rank
    ['Panama']
    """
    return [
        element.attrib.get(attr_name)
        for element in elements
    ]


def get_task_names(
        root: xml.etree.ElementTree.Element,
        xml_tag: str,
        xml_attr: str,
        attr_val: str,
        target: str = "sourceDir"
        ) -> List[Union[str, None]]:
    """
    Return the list of all names from the given XML.

    :param root: an object with the content of the XML file.
    :type root: xml.etree.ElementTree.Element
    :param xml_tag: a name of XML element.
    :type xml_tag: str
    :param xml_attr: a name of the element attribute.
    :type xml_tag: str
    :param attr_val: a value of XML element attribute.
    :type attr_val: str
    :return: a list of all searched attribute values with relative paths.
    :rtype: list

    :Example:
    >>> import xml.etree.ElementTree
    >>> test_xml = "src/tests/foo.xml"
    >>> tree = xml.etree.ElementTree.parse(test_xml)
    >>> root = tree.getroot()
    >>> output = get_task_names(root, "country", "name", "P", "name")
    >>> output
    ['Panama']
    """
    elems = get_specific_elements(root, xml_tag, xml_attr, attr_val)
    return select_attr_value(elems, target)


def create_task_data(
    task_paths: List[Union[str, None]]
        ) -> Dict[str, Dict[str, Optional[str]]]:
    """
    Return the dictionary with the task names (keys) and the nested dictionaries
    with the attributes.

    :Example:
    >>> create_task_data(("hhh/kkk/sss/ddd",))
    {'sss': {'folder': 'hhh', 'lesson': 'kkk', 'path': 'hhh/kkk/sss/ddd'}}
    """
    tasks = dict()

    for task_path in task_paths:
        folder, lesson, name = parse_name(task_path)
        tasks[name] = {
            "folder": folder,
            "lesson": lesson,
            "path": task_path
        }

    return tasks


def parse_name(path: Union[str, None]) -> Tuple[str, str, str]:
    """
    From the given name parse folder, lesson and task name.

    :Example:
    >>> parse_name("foo/bar/fii/doo")
    ('foo', 'bar', 'fii')
    >>> parse_name("bar/foo/fii/doo")
    ('bar', 'foo', 'fii')
    """
    try:
        if path:
            folder, lesson, name, _ = path.split("/")

    except Exception:
        output = "", "", ""
    else:
        output = folder, lesson, name
    finally:
        return output


def get_only_task_name(data: Dict[str, str]) -> Tuple[str, ...]:
    """
    Return only the tuple of names.

    :param data: a dictionary with the path details.
    :type data: dict
    :return: a sequence of values from the parsed keys 'name'.
    :rtype: a tuple

    :Example:
    >>> get_only_task_name(
    ...     {"task1":
    ...         {"folder": "a", "lesson": "L01", "path": "foo"},
    ...     "task2":
    ...         {"folder": "b", "lesson":"L02", "path": "bar"}
    ...     }
    ... )
    ('task1', 'task2')
    """
    return tuple(data.keys())
