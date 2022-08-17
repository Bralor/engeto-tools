import xml.etree.ElementTree
from typing import List, Dict, Union

import task_manager.utils as tu
from task_manager.description import load_lesson_tasks


def replace_attributes(
        tree: xml.etree.ElementTree.ElementTree,
        exercises: List[xml.etree.ElementTree.Element],
        new_path: Dict[str, Dict[str, str]]
        ) -> None:
    """
    Replace attributes in the given exercise elements.

    :param tree: an object that represents XML content.
    :type tree: xml.etree.ElementTree.ElementTree
    :param exercises: an sequence of exercise elements.
    :type exercises: list
    :param new_path: an updated value of relative path.
    :type new_path: str
    """
    update_all(exercises, new_path)
    tree.write("output_attr.xml", encoding="utf-8")


def update_all(
        exercises: List[xml.etree.ElementTree.Element],
        new_path: Dict[str, Dict[str, str]]
) -> None:
    """
    In the list of exercises, update the specific attribute with new value.

    :param exercises: a sequence of exercises from the XML source.
    :type exercises: list
    :param new_path: an updated value of relative path.
    :type new_path: str

    :Example:
    >>> import xml.etree.ElementTree as te
    >>> tree = te.parse("src/tests/bar.xml")
    >>> root = tree.getroot()
    >>> exercises = [exercise for exercise in root.iter("exercise")]
    >>> out = {'Rozdělení stringu': {'perex': 'nan_sourceDir',
    ...     'skeleton': 'exercises/L01/rozdeleni_stringu/skeleton',
    ...     'unit-tests': 'nan_sourceDir',
    ...     'solution': 'exercises/L01/rozdeleni_stringu/solution',
    ...     'description': 'exercises/L01/rozdeleni_stringu/skeleton'},
    ...     'Spojování stringů': {'perex': 'nan_sourceDir',
    ...     'skeleton': 'exercises/L01/spojovani_stringu/skeleton',
    ...     'solution': 'exercises/L01/spojovani_stringu/solution',
    ...     'description': 'exercises/L01/spojovani_stringu/skeleton'}}
    >>> update_all(exercises, out)
    >>> exercises[0].find("skeleton").attrib["sourceDir"]
    'exercises/L01/rozdeleni_stringu/skeleton'
    >>> exercises[1].find("skeleton").attrib["sourceDir"]
    'exercises/L01/spojovani_stringu/skeleton'
    """
    for exercise in exercises:
        update_exercise(
            exercise, new_path[exercise.attrib["name"]],  # type: ignore
            "sourceDir", "skeleton", "unit-tests", "description", "solution"
        )


def update_exercise(
        exercise: xml.etree.ElementTree.Element,
        new_path: Dict[str, str],
        attr_name: str,
        *children
        ) -> None:
    """
    Update all the attribute values in a single 'exercise' tag.

    :param exercise: an object that represents specific task element.
    :type exercise: xml.etree.ElementTree.Element
    :param new_path: a relative path of task folder.
    :type new_path: str
    :param attr_name: a name of the attribute.
    :type attr_name: str
    :param children: a sequence of children elements.
    :type children: tuple

    :Example:
    >>> import xml.etree.ElementTree as te
    >>> tree = te.parse("src/tests/bar.xml")
    >>> root = tree.getroot()
    >>> out = {'Rozdělení stringu': {'perex': 'nan_sourceDir',
    ...     'skeleton': 'exercises/L01/rozdeleni_stringu/skeleton',
    ...     'unit-tests': 'nan_sourceDir',
    ...     'solution': 'exercises/L01/rozdeleni_stringu/solution',
    ...     'description': 'exercises/L01/rozdeleni_stringu/skeleton'},
    ...     'Spojování stringů': {'perex': 'nan_sourceDir',
    ...     'skeleton': 'exercises/L01/spojovani_stringu/skeleton',
    ...     'solution': 'exercises/L01/spojovani_stringu/solution',
    ...     'description': 'exercises/L01/spojovani_stringu/skeleton'}}
    >>> exercises = [exercise for exercise in root.iter("exercise")]
    >>> update_exercise(
    ...     exercises[0], out[exercises[0].attrib["name"]],
    ...     "sourceDir", "skeleton", "unit-tests"
    ... )
    >>> exercises[0].find("skeleton").attrib["sourceDir"]
    'exercises/L01/rozdeleni_stringu/skeleton'
    >>> exercises[0].find("unit-tests").attrib["src"]
    'nan_sourceDir'
    """
    for child in children:
        if child == "unit-tests":
            update_attribute(
                exercise.find(child), "src", new_path.get(child)
            )
        else:
            update_attribute(
                exercise.find(child), attr_name, new_path.get(child)
            )


def update_attribute(
        task_element: Union[xml.etree.ElementTree.Element, None],
        attr_name: str,
        attr_val: Union[str, None]
        ) -> str:
    """
    Return a selected attribute with updated value.

    :param task_element: an object with selected XML children.
    :type task_element: xml.etree.ElementTree.Element
    :param attr_name: a name of the attribute.
    :type attr_name: str
    :param attr_val: a new value of the attribute.
    :type attr_val: str
    :return: an overwritten value of the attribute.
    :rtype: str

    :Example:
    >>> import xml.etree.ElementTree as te
    >>> tree = te.parse("src/tests/foo.xml")
    >>> root = tree.getroot()
    >>> countries = [country for country in root.iter("country")]
    >>> update_attribute(countries[0].find("neighbor"), "name", "Germany")
    'Germany'
    """
    try:
        task_element.attrib[attr_name] = attr_val  # type: ignore

    except BaseException:
        output = "Cannot find the element"
    else:
        output = task_element.attrib[attr_name] if task_element else ""
    finally:
        return output


def collect_data(
    exercises: List[xml.etree.ElementTree.Element]
        ) -> Dict[str, Dict[str, str]]:
    """
    From the given pool of exercises returns a object with names and attributes.

    :param exercises: an object with all task elements.
    :type exercises: list
    :return: an object with task names as keys and attributes as values.
    :rtype: dict

    :Example:
    >>> import xml.etree.ElementTree as te
    >>> tree = te.parse("src/tests/bar.xml")
    >>> root = tree.getroot()
    >>> exercises = [exercise for exercise in root.iter("exercise")]
    >>> out = collect_data(exercises)
    >>> out['Rozdělení stringu']['perex']
    'nan_sourceDir'
    """
    return {
        exercise.attrib.get("name", "nan_name"): collect_task_data(exercise)
        for exercise in exercises
    }


def collect_task_data(
    exercise: xml.etree.ElementTree.Element
        ) -> Dict[str, str]:
    """
    From the given task element 'exercise' return a dictionary with attributes.

    :param exercise: an object with selected XML children.
    :type exercise: xml.etree.ElementTree.Element
    :return: an object with tasks attributes.
    :rtype: dict

    :Example:
    >>> import xml.etree.ElementTree as te
    >>> tree = te.parse("src/tests/bar.xml")
    >>> root = tree.getroot()
    >>> exercises = [exercise for exercise in root.iter("exercise")]
    >>> out = collect_task_data(exercises[0])
    >>> out["skeleton"]
    'exercises/L01/slicing_string/skeleton'
    >>> out["unit-tests"]
    'exercises/L01/slicing_string/tests.py'
    """
    data = dict()

    for element in list(exercise):
        if element.tag == "unit-tests":
            data[element.tag] = element.attrib.get("src", "nan_sourceDir")
        else:
            data[element.tag] = element.attrib.get("sourceDir", "nan_sourceDir")

    return data


def replace_values(
    data: Dict[str, Dict[str, str]]
        ) -> Dict[str, Dict[str, str]]:
    """
    Return an object with replaced values of the old attributes.

    :param data: an object with parsed data from the attributes.
    :type data: dict
    :return: an object with an update values.
    :rtype: dict

    :Example:
    >>> from task_manager.utils import lesson01
    >>> out = {'Rozdělení stringu': {'perex': 'nan_sourceDir',
    ...     'description': 'exercises/L01/rozdeleni_stringu/skeleton'},
    ...     'Spojování stringů': {'perex': 'nan_sourceDir',
    ...     'solution': 'exercises/L01/spojovani_stringu/solution',
    ...     'description': 'exercises/L01/spojovani_stringu/skeleton'}}
    >>> replace_values(out)['Rozdělení stringu']['description']
    'exericses/L01/rozdeleni_stringu/skeleton'
    """
    for key_out, value in data.items():
        for key_in, val in value.items():
            if val != "nan_sourceDir":
                root, lesson, name, subdir = val.split("/")
                updated = load_lesson_tasks(
                    tu.lessons.get(lesson, "nan_lesson")
                ).get(name, "nan_name")

                if updated == "nan_name":
                    continue
                data[key_out][key_in] = "/".join(
                    (root, lesson, updated, subdir)
                )
    return data

