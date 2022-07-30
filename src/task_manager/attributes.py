import xml.etree.ElementTree


def replace_attributes(
        tree: xml.etree.ElementTree.ElementTree,
        exercises: list,
        new_path: dict
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
    tree.write("output_attrs.xml", encoding="utf-8")


def update_all(exercises: list, new_path: dict) -> None:
    """
    In the list of exercises, update the specific attribute with new value.

    :param exercises: a sequence of exercises from the XML source.
    :type exercises: list
    :param new_path: an updated value of relative path.
    :type new_path: str

    :Example:
    >>> import xml.etree.ElementTree as te
    >>> tree = te.parse("srcTests/tests/bar.xml")
    >>> root = tree.getroot()
    >>> exercises = [exercise for exercise in root.iter("exercise")]
    >>> out = {'Rozdělení stringu': {'perex': 'nan_sourceDir',
    ...     'exercise-folder': 'exercises/L01/rozdeleni_stringu/exercise-folder',
    ...     'tests': 'nan_sourceDir',
    ...     'solution': 'exercises/L01/rozdeleni_stringu/solution',
    ...     'description': 'exercises/L01/rozdeleni_stringu/exercise-folder'},
    ...     'Spojování stringů': {'perex': 'nan_sourceDir',
    ...     'exercise-folder': 'exercises/L01/spojovani_stringu/exercise-folder',
    ...     'solution': 'exercises/L01/spojovani_stringu/solution',
    ...     'description': 'exercises/L01/spojovani_stringu/exercise-folder'}}
    >>> update_all(exercises, out)
    >>> exercises[0].find("exercise-folder").attrib["sourceDir"]
    'exercises/L01/rozdeleni_stringu/exercise-folder'
    >>> exercises[1].find("exercise-folder").attrib["sourceDir"]
    'exercises/L01/spojovani_stringu/exercise-folder'
    """
    for exercise in exercises:
        update_exercise(
            exercise, new_path[exercise.attrib["name"]], "sourceDir",
            "exercise-folder", "tests", "description", "solution")


def update_exercise(
        exercise: xml.etree.ElementTree.Element,
        new_path: dict,
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
    >>> tree = te.parse("srcTests/tests/bar.xml")
    >>> root = tree.getroot()
    >>> out = {'Rozdělení stringu': {'perex': 'nan_sourceDir',
    ...     'exercise-folder': 'exercises/L01/rozdeleni_stringu/exercise-folder',
    ...     'tests': 'nan_sourceDir',
    ...     'solution': 'exercises/L01/rozdeleni_stringu/solution',
    ...     'description': 'exercises/L01/rozdeleni_stringu/exercise-folder'},
    ...     'Spojování stringů': {'perex': 'nan_sourceDir',
    ...     'exercise-folder': 'exercises/L01/spojovani_stringu/exercise-folder',
    ...     'solution': 'exercises/L01/spojovani_stringu/solution',
    ...     'description': 'exercises/L01/spojovani_stringu/exercise-folder'}}
    >>> exercises = [exercise for exercise in root.iter("exercise")]
    >>> update_exercise(
    ...     exercises[0], out[exercises[0].attrib["name"]],
    ...     "sourceDir", "exercise-folder", "tests"
    ... )
    >>> exercises[0].find("exercise-folder").attrib["sourceDir"]
    'exercises/L01/rozdeleni_stringu/exercise-folder'
    >>> exercises[0].find("tests").attrib["srcTests"]
    'nan_sourceDir'
    """
    for child in children:
        if child == "tests":
            update_attribute(
                exercise.find(child), "srcTests", new_path.get(child)
            )
        else:
            update_attribute(
                exercise.find(child), attr_name, new_path.get(child)
            )


def update_attribute(
        task_element: xml.etree.ElementTree.Element,
        attr_name: str,
        attr_val: str
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
    >>> tree = te.parse("srcTests/tests/foo.xml")
    >>> root = tree.getroot()
    >>> countries = [country for country in root.iter("country")]
    >>> update_attribute(countries[0].find("neighbor"),"name","Czech republic")
    'Czech republic'
    """
    try:
        task_element.attrib[attr_name] = attr_val

    except BaseException:
        output = "Cannot find the element"
    else:
        output = task_element.attrib[attr_name]
    finally:
        return output


def collect_data(exercises: list) -> dict:
    """
    From the given pool of exercises returns a object with names and attributes.

    :param exercises: an object with all task elements.
    :type exercises: list
    :return: an object with task names as keys and attributes as values.
    :rtype: dict

    :Example:
    >>> import xml.etree.ElementTree as te
    >>> tree = te.parse("srcTests/tests/bar.xml")
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


def collect_task_data(exercise: xml.etree.ElementTree.Element) -> dict:
    """
    From the given task element 'exercise' return a dictionary with attributes.

    :param exercise: an object with selected XML children.
    :type exercise: xml.etree.ElementTree.Element
    :return: an object with tasks attributes.
    :rtype: dict

    :Example:
    >>> import xml.etree.ElementTree as te
    >>> tree = te.parse("srcTests/tests/bar.xml")
    >>> root = tree.getroot()
    >>> exercises = [exercise for exercise in root.iter("exercise")]
    >>> out = collect_task_data(exercises[0])
    >>> out["exercise-folder"]
    'exercises/L01/slicing_string/exercise-folder'
    >>> out["tests"]
    'exercises/L01/slicing_string/tests.py'
    """
    data = dict()

    for element in list(exercise):
        if element.tag == "tests":
            data[element.tag] = element.attrib.get("srcTests", "nan_sourceDir")
        else:
            data[element.tag] = element.attrib.get("sourceDir", "nan_sourceDir")

    return data


def replace_values(data: dict, pattern: dict) -> dict:
    """
    Return an object with replaced values of the old attributes.

    :param data: an object with parsed data from the attributes.
    :type data: dict
    :param pattern: an object with keys as a current data and values as
        an updated value.
    :type pattern: dict
    :return: an object with an update values.
    :rtype: dict

    :Example:
    >>> from srcTests.task_manager.utils import lesson01
    >>> out = {'Rozdělení stringu': {'perex': 'nan_sourceDir',
    ...     'exercise-folder': 'exercises/L01/rozdeleni_stringu/exercise-folder',
    ...     'tests': 'nan_sourceDir',
    ...     'solution': 'exercises/L01/rozdeleni_stringu/solution',
    ...     'description': 'exercises/L01/rozdeleni_stringu/exercise-folder'},
    ...     'Spojování stringů': {'perex': 'nan_sourceDir',
    ...     'exercise-folder': 'exercises/L01/spojovani_stringu/exercise-folder',
    ...     'solution': 'exercises/L01/spojovani_stringu/solution',
    ...     'description': 'exercises/L01/spojovani_stringu/exercise-folder'}}
    >>> replace_values(out, lesson01)['Rozdělení stringu']['description']
    'exericses/L01/rozdeleni_stringu/exercise-folder'
    """
    for key_out, value in data.items():
        for key_in, val in value.items():
            if val != "nan_sourceDir":
                root, lesson, name, subdir = val.split("/")
                data[key_out][key_in] = "/".join(
                    (root, lesson, pattern.get(name), subdir)
                )
    return data


if __name__ == "__main__":
    import doctest
    doctest.testmod()
