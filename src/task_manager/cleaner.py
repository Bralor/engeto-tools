import os
import shutil
import xml.etree.ElementTree


def select_names(exercises: list) -> set:
    """
    Return an object of task names.

    :param exercises: a sequence of XML elements.
    :type exercises: list
    :return: an object with the names.
    :rtype: set

    :Example:
    >>> import xml.etree.ElementTree as et
    >>> tree = et.parse("src/tests/bar.xml")
    >>> root = tree.getroot()
    >>> exercises = [exercise for exercise in root.iter("exercise")]
    >>> print(select_names(exercises))
    {'string_operations', 'slicing_string'}
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
    >>> import xml.etree.ElementTree as et
    >>> tree = et.parse("src/tests/bar.xml")
    >>> root = tree.getroot()
    >>> exercises = [exercise for exercise in root.iter("exercise")]
    >>> print(select_attr(exercises[0], "solution", "sourceDir"))
    exercises/L01/slicing_string/solution
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

    :Example:
    >>> result = split_name("foo/bar/boo/bar")
    >>> result
    'boo'
    """
    try:
        _, _, name, _ = path.split("/")

    except BaseException:
        output = ""
    else:
        output = name
    finally:
        return output


def remove_unused_lessons(lessons: list, target: str, rel_path: str) -> None:
    """
    Remove all the directories in the given sequence except of the target.

    :param lessons: a sequence of files.
    :type lessons: list
    :param target: name of the target.
    :type target: str
    :param rel_path: a relative path to the lesson.
    :type target: str
    """
    for folder in lessons:
        if folder != target:
            shutil.rmtree(os.path.join(rel_path, folder))


def rename_dirs(dirs: tuple, pattern: dict, package: str) -> None:
    """
    Rename the given sequence of directories according to the pattern.

    :param dirs: a sequence of folders.
    :type dirs: tuple
    :param pattern: a mapping object with keys as current names.
    :type pattern: dict
    :param package: a relative path of the package.
    :type package: str

    """
    for folder in os.listdir(package):
        print(folder)
        if not os.path.exists(os.path.join(package, folder)):
            continue

        updated_name = pattern.get(folder)
        os.rename(os.path.join(package, folder),
                  os.path.join(package, updated_name))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
