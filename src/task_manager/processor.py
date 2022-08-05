import os

import task_manager.utils as tu

from task_manager.parser import get_xml_root

from task_manager.description import replace_descriptions

from task_manager.tasknames import create_task_data
from task_manager.tasknames import get_all_tasks, get_task_names

from task_manager.attributes import replace_values, collect_data, replace_attributes

from task_manager.cleaner import remove_unused_lessons
from task_manager.cleaner import rename_dirs, move_content


def task_desc_processor(engeto: str, task_p: str) -> None:
    """
    Run the processor of the descriptions in a XML source file.
    """
    rel_path = os.path.join(engeto, f"course_{os.path.basename(engeto)}.xml")
    tree = get_xml_root(rel_path)

    exercises = get_all_tasks(tree.getroot(), "exercise")
    task_names = get_task_names(
        tree.getroot(), "solution",
        "sourceDir", "exercises/"
    )
    task_data = create_task_data(task_names)
    replace_descriptions(tree, task_data, exercises, task_p)


def task_attr_processor(source: str) -> None:
    """
    Run the main function for the overwritting the attributes.
    """
    tree = get_xml_root(source)
    exercises = get_all_tasks(tree.getroot(), "exercise")

    task_data = replace_values(collect_data(exercises))
    replace_attributes(tree, exercises, task_data)


def task_content_processor(
        engeto_repo: str,
        lesson_num: str,
        ) -> None:
    """
    Run the main function and remove all the unused lesson and tasks.
    """
    for key, value in tu.lessons.items():
        if value == lesson_num:
            lesson = key

    remove_unused_lessons(
        os.listdir(os.path.join(engeto_repo, "exercises")),
        lesson,
        os.path.join(engeto_repo, "exercises")
    )

    rename_dirs(
        tuple(os.listdir(os.path.join(engeto_repo, "exercises", lesson))),
        lesson_num,
        os.path.join(engeto_repo, "exercises", lesson)
    )

    move_content(
        os.path.join(engeto_repo, "exercises", lesson),
        engeto_repo,
        os.path.join("../engeto_tasks/tasks", lesson_num)
    )
