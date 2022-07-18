"""
src/processor.py - Task processor.
"""
import os

from src.parser import get_xml_root

from src.tasks.tasknames import get_all_tasks
from src.tasks.tasknames import get_task_names
from src.tasks.tasknames import create_task_data

from src.description import replace_descriptions


def task_processor():
    """
    Run the main runner of the package.
    """
    # temporary hardwired arguments
    arg_1 = "-t"
    arg_2 = "../python-uvod-do-programovani"
    arg_3 = "course_python-uvod-do-programovani.xml"
    arg_4 = "../engeto_tasks/"

    # get tree of XML and parse the content
    rel_path = os.path.join(arg_2, arg_3)
    tree = get_xml_root(rel_path)

    # get XML tags
    exercises = get_all_tasks(tree.getroot(), "exercise")

    # get task names and task data
    task_names = get_task_names(
        tree.getroot(), "solution",
        "sourceDir", "exercises/"
    )
    task_data = create_task_data(task_names)

    output = replace_descriptions(tree, task_data, exercises)


    print("Done!")
    return output


def task_attr_processor():
    """
    Run the main function for the overwritting the attributes.
    """
