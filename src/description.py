import os
import xml.etree.ElementTree


def replace_descriptions(
        tree: xml.etree.ElementTree.Element,
        names: list,
        exercises: list
    ) -> None:
    """
    Update the XML tree with the given task names and task elements.

    :param tree:
    :type tree:
    :param names:
    :type names:
    :param exercises:
    :type exercises:
    :return: nothing
    :rtype:

    :Example:
    """
    # for taskname, exercise in zip(names, exercises):
        # description = process_description(tree, taskname, exercise)
        # update_element(select_attribute(exercise, "description"), description)

    # else:
        # update_element(select_attribute(exercise, "solution"), "")
        # update_root(tree, "test_output.xml")
    pass


def process_description(tree, name: str, exercise) -> str:
    """
    Read the content of created README.md paths. Then insert the readed text
    into the tree.

    :param tree:
    :type tree:
    :param name:
    :type name:
    :param exercise:
    :type exercise:
    :return:
    :rtype:

    :Example:
    """
    # readme_path = select_specific_doc("../engeto_tasks/tasks", "lesson01",
        # lesson01.get(name, "nan_task"))
    # content = load_description(readme_path)
    # return process_the_text(content)
    pass


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
    >>> import utils.tasks_pattern as tp
    >>> print(get_current_name("slicing_string", tp.pattern))
    'rozdeleni_stringu'
    >>> print(get_current_name("non_existing_t", tp.pattern))
    'nan_task'
    """
    return pattern.get(old_name, "nan_task")


def get_current_lesson(name: str, data: dict, pattern: dict) -> str:
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
    >>> import utils.lesson_pattern.py as lp
    >>> exerc_1 = {
    ...    'slicing_string' : {
    ...         'folder': 'exercises',
    ...         'lesson': 'L01',
    ...         'path': 'exercises/L01/slicing_string/solution'
    ...     }
    ... }
    >>> print(get_current_lesson("slicing_string", exerc_1, lp.lessons))
    'lesson01'
    """
    return pattern.get(data.get(name), "nan_lesson")


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
    >>> print(read_description("rozdeleni_stringu", "lesson01")[5])
    'V této úloze budeš pracovat s indexy datového typu 'str'.\\n'
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


def write_description():
    """
    Write a description of text inside the specific XML element.

    :Example:
    >>>
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
