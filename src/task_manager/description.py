import os
import logging
import xml.etree.ElementTree
from typing import Dict, List, Tuple, Optional

import task_manager.utils as tu

from task_manager.text_processor import process_text


def replace_descriptions(
        tree: xml.etree.ElementTree.ElementTree,
        data: Dict[str, Dict[str, Optional[str]]],
        exercises: List[xml.etree.ElementTree.Element],
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
        process_description(task_data, package)
        remove_solution(exercise)

    tree.write("output_desc.xml", encoding="utf-8")


def remove_solution(exercise: xml.etree.ElementTree.Element) -> None:
    """
    From the given tag remove the current text.

    :param exercise: an xml element with task.
    :type exercise: xml.etree.ElementTree.Element
    """
    try:
        solution_tag = exercise.find("solution")

    except Exception:
        logging.warning(f"No childern element: {exercise}")
    else:
        if hasattr(solution_tag, "text"):
            solution_tag.text = ""  # type: ignore
        else:
            logging.warning("Missing attribute 'text'.")


def process_description(
        task_data: Tuple[str, Dict[str, Optional[str]]],
        package: str
        ) -> None:
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
    lesson = load_lesson_tasks(
        tu.lessons.get(task_data[1]["lesson"], "nan_lesson")   # type: ignore
    )
    name = get_current_name(task_data[0], lesson)

    if lesson != "nan_lesson" and name != "nan_task":          # type: ignore
        lesson_nr = get_current_lesson(task_data, tu.lessons)  # type: ignore
        process_text(
            read_description(
                package, name, lesson_nr
            )
        )


def load_lesson_tasks(lesson: str) -> Dict[str, str]:
    """
    Return an object with the name mapping for the specific lesson.
    """
    try:
        value = getattr(globals()["tu"], lesson)

    except AttributeError:
        output = {}
    else:
        output = value
    finally:
        return output


def get_current_name(old_name: str, pattern: Dict[str, str]) -> str:
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


def get_current_lesson(
    data: Tuple[str, Dict[str, str]],
    pattern: Dict[str, str]
) -> str:
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
    return pattern.get(attrib.get("lesson"), "nan_lesson")  # type: ignore


def read_description(pack_path: str, name: str, lesson: str) -> List[str]:
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
        logging.warning(f"Path does not exist: tasks/{lesson}/{name}/README.md")
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
    description_tag.text = text  # type: ignore
    return description_tag.text  # type: ignore
