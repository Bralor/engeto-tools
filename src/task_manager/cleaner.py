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

    return {
        split_name(
            select_attr(exercise, "solution", "sourceDir")
        )
        for exercise in exercises
    }


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


def split_name(path: str) -> str:
    """
    Return a parsed name from the relative path.

    :param path: a relative path to the file.
    :type path: str
    :return: a name of the task.
    :rtype: str
    """
    try:
        _, _, name , _ = path.split("/")

    except BaseException:
        output = ""
    else:
        output = name
    finally:
        return output

