"""
src/processor.py - Task processor.
"""
import os

from src.parser.parser import get_xml_root
from src.parser.parser import set_xml_attr

from src.tasks.tasknames import get_all_tasks
from src.tasks.tasknames import get_task_names
from src.tasks.tasknames import create_task_data
from src.tasks.tasknames import get_only_task_name


def task_processor():
    """
    Run the main runner of the package.
    """
    arg_1 = "-t"
    arg_2 = "../python-uvod-do-programovani"
    arg_3 = "course_python-uvod-do-programovani.xml"

    # get tree of XML and parse the content
    rel_path = os.path.join(arg_2, arg_3)

    tree = get_xml_root(rel_path)
    params = set_xml_attr(tag="solution", name="sourceDir", value="exercises/")

    # get XML tags
    exercise_tags = get_all_tasks(tree.getroot(), "exercise")

    # get task paths and task data
    task_names = get_task_names(tree.getroot(), params)
    task_data = create_task_data(task_names)

    # get only names
    only_names = get_only_task_name(task_data)

    print("Done!")
    return only_names

