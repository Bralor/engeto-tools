import os
import xml.etree.ElementTree

from task_manager.utils import lessons, lesson01

from task_manager.text_processor import process_text


def replace_descriptions(
        tree: xml.etree.ElementTree.ElementTree,
        data: dict,
        exercises: list,
        package: str
    ) -> None:
    """
    Update the XML tree with the given task names and task elements.

    :param tree: an object that represents XML content.
    :type tree: xml.etree.ElementTree.ElementTree
    :param data: an object with tasks attributes.
    :type data: dict
    :param exercises: an sequence of exercise elements.
    :type exercises: list
    """
    for task_data, exercise in zip(data.items(), exercises):
        report = process_description(task_data, exercise, package)
        print(report[:50])

    tree.write("output_descr.xml", encoding="utf-8")


def process_description(
        task_data: tuple,
        exercise: xml.etree.ElementTree.Element,
        package: str
    ) -> str:
    """
    Read the content of created README.md paths. Then insert the readed text
    into the tree.

    :param task_data: an object with task attributes.
    :type name: tuple
    :param exercise: an object that represents single exercise.
    :type exercise: xml.etree.ElementTree.Element
    :param package: a name of the package.
    :type package: str
    :return: an overwritten text.
    :rtype: str
    """
    name = get_current_name(task_data[0], lesson01)
    lesson_nr = get_current_lesson(task_data, lessons)
    processed_txt = process_text(
        read_description(
            package, name, lesson_nr
        )
    )
    return write_description(processed_txt, exercise)


def get_current_name(old_name: str, pattern: dict) -> str:
    """
    Return the current name of the task, based on the given pattern.

    :param old_name: an previous name of the task.
    :type old_name: str
    :param pattern: an object with the mapping pattern.
    :type pattern: dict
    :return: an updated name of the task.
    :rtype: str

    :Example:
    >>> pattern = {"slicing_string": "rozdeleni_stringu"}
    >>> print(get_current_name("slicing_string", pattern))
    rozdeleni_stringu
    >>> print(get_current_name("non_existing_t", pattern))
    nan_task
    """
    return pattern.get(old_name, "nan_task")


def get_current_lesson(data: tuple, pattern: dict) -> str:
    """
    Return the lesson name of the task, based on the given pattern.

    :param name: an previous name of the task.
    :type name: str
    :param data: an attributes of the given task
    :type data: dict
    :param pattern: an object with the mapping pattern.
    :type pattern: dict
    :return: an updated name of the task.
    :rtype: str

    :Example:
    >>> lessons = {"L01": "lesson01"}
    >>> exerc_1 = (
    ...    'slicing_string', {
    ...         'folder': 'exercises',
    ...         'lesson': 'L01',
    ...         'path': 'exercises/L01/slicing_string/solution'
    ...     }
    ... )
    >>> print(get_current_lesson(exerc_1, lessons))
    lesson01
    """
    _, attrib = data
    return pattern.get(attrib.get("lesson"), "nan_lesson")


def read_description(pack_path: str, name: str, lesson: str) -> list:
    """
    Return the list that contents description of the certain task.

    :param pack_path: a relative path of the package.
    :type pack_path: str
    :param name: an previous name of the task.
    :type name: str
    :param lesson: a name of the lesson.
    :param lesson: str
    :return: a content of the README.md file.
    :rtype: list

    :Example:
    >>> print(read_description(
    ...     "../engeto_tasks", "rozdeleni_stringu", "lesson01")[5]
    ... )
    V této úloze budeš pracovat s indexy datového typu `str`.
    <BLANKLINE>
    """
    try:
        with open(
            os.path.join(pack_path, "tasks", lesson, name, "README.md")
        ) as md:
            content = md.readlines()

    except FileNotFoundError:
        output = []
    else:
        output = content
    finally:
        return output


def write_description(
        text: str,
        selected_element: xml.etree.ElementTree.Element,
        child: str = "description"
    ) -> str:
    """
    Write a description of text inside the specific XML element.

    :param text: a new task description.
    :type text: str
    :param selected_element: an element with task.
    :type param: xml.etree.ElementTree.Element
    :param child: a name of the children tag.
    :type child:
    :return: a content of new tag
    :rtype: str

    :Example:
    >>> import xml.etree.ElementTree as te
    >>> tree = te.parse("src/tests/foo.xml")
    >>> root = tree.getroot()
    >>> countries = [country for country in root.iter("country")]
    >>> print(write_description("XXXX", countries[0], "year"))
    XXXX
    """
    description_tag = selected_element.find(child)
    description_tag.text = text
    return description_tag.text



if __name__ == "__main__":
    import doctest
    doctest.testmod()
