import xml.etree.ElementTree


def select_names(exercises: list, lesson: dict) -> set:
    """
    Return an object of task names.

    :param exercises: a sequence of XML elements.
    :type exercises: list
    :return: an object with the names.
    :rtype: set

    :Example:
    >>>
    """
    new_names = set()

    for exercise in exercises:
        solution = exercise.find("solution")
        path = solution.attrib.get("sourceDir", "nan_path")
        _, _, name , _ = path.split("/")
        new_names.add(lesson.get(name))

    return new_names


def select_attr(
        element: xml.etree.ElementTree.Element,
        child: str,
        attr_name: str
    ) -> str:
    """
    Return a string from the attribute with a path.

    :param element: an exercise element of XML file.
    :type element: xml.etree.ElementTree.Element
    :param child: a name of the child
    :type child: str
    :param attr_name:
    :type attr_name:
    :return:
    :rtype:

    :Example:
    >>>
    """
    solution = element.find(child)
    return solution.attrib.get(attr_name, "nan_path")
