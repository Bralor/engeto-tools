import os
import shutil
import xml.etree.ElementTree

import task_manager.utils as tu

from task_manager.description import load_lesson_tasks


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


def rename_dirs(dirs: tuple, pattern: str, package: str) -> None:
    """
    Rename the given sequence of directories according to the pattern.

    :param dirs: a sequence of folders.
    :type dirs: tuple
    :param pattern: a mapping object with keys as current names.
    :type pattern: dict
    :param package: a relative path of the package.
    :type package: str
    """
    for folder in dirs:
        if not os.path.exists(os.path.join(package, folder)):
            continue
        updated = load_lesson_tasks(pattern).get(folder)

        if not updated:
            shutil.rmtree(os.path.join(package, folder))
            continue
        os.rename(os.path.join(package, folder),
                  os.path.join(package, updated))


def move_content(lesson_path: str, engeto_repo: str, package: str) -> None:
    """
    Move the content of the task folder from the package to the repository.

    :param dirs: a sequence of all the czech task names.
    :type dirs: tuple
    :param engeto_repo: a relative path to the repository.
    :type engeto_repo: str
    :param package: a relative path to the package.
    :type package: str

    """
    lesson = os.path.basename(lesson_path)

    for folder in os.listdir(lesson_path):
        enge_solution = os.path.join(
            engeto_repo, "exercises", lesson, folder, "solution"
        )
        pack_solution = os.path.join(package, folder)

        if not os.path.exists(enge_solution) \
                or not os.path.exists(pack_solution):
            continue
        shutil.copyfile(
            os.path.join(pack_solution, f"{folder}.py"),
            os.path.join(enge_solution, "main.py")
        )

    # lesson = os.path.basename(lesson_path)  # L04
    # # package_lesson = os.path.basename(package)

    # # existing_tasks = load_lesson_tasks(tu.lessons.get(lesson, "nan_folder"))
    # # moved = list()

    # for folder in os.listdir(lesson_path):
        # if folder not in existing_tasks:
            # continue
        # pack_solution = os.path.join(package, folder)
        # enge_solution = os.path.join(
            # engeto_repo, "exercises", lesson, folder, "solution"
        # )
        # # print(enge_solution)
        # # print(pack_solution)

        # if not os.path.exists(enge_solution) \
                # or not os.path.exists(pack_solution):
            # continue
        # shutil.copyfile(
            # os.path.join(pack_solution, f"{folder}.py"),
            # os.path.join(enge_solution, "main.py")
        # )
        # moved.append(load_lesson_tasks(package_lesson).get(folder))

    # # diff = set(moved)
    # # diff = diff.add("__init__.py")
    # # for folder in set(os.listdir(package)).difference(diff):
        # # if os.path.exists(os.path.join(lesson_path, folder)):
            # # continue
        # # pack_solution = os.path.join(package, folder)
        # # enge_solution = os.path.join(
            # # engeto_repo, "exercises", lesson, load_lesson_tasks(tu.lessons.get(lesson)).get(folder), "solution"
        # # )
        # # print(pack_solution)
        # # print(enge_solution)

        # # shutil.copyfile(
            # # os.path.join(pack_solution, f"{folder}.py"),
            # # os.path.join(enge_solution, "main.py")
        # # )


def add_missing_task(engeto_tasks: str, package_tasks: str) -> None:
    """
    Create a task folder with content if the task is not part of current
    repository.

    :Example:
    >>> package = "../engeto_tasks/tasks/lesson04"
    >>> repository = "../python-for-cyklus/exercise/L04"
    >>> add_missing_task(package, repository)
    """
    repository = set(os.listdir(engeto_tasks))
    package = set(os.listdir(package_tasks))
    diff = package.difference(repository)

    for file in diff:
        rel_path_repo = os.path.join(package_tasks, file)

        if file != "__init__.py":
            # print(rel_path_repo)
            # print(engeto_tasks)
            # print(package_tasks)
            create_task_folder(rel_path_repo, engeto_tasks, package_tasks)


def create_task_folder(rel_path: str, repository: str, package: str) -> None:
    """
    Create a new folder for the missing task. Then create subfolders 'skeleton'
    'solution' and the file 'skeleton/main.py'.

    :param rel_path: a relative path of the folder.
    :type rel_path: str
    :param repository: a relative path of the new folder.
    :type repository: str
    :param package: a relative path of the pattern task folder.
    :type package: str
    """
    # os.mkdir(rel_path)
    print("creating...", repository)

    for subfolder in "skeleton", "solution":
        print("creating subs..", subfolder)
        # os.mkdir(os.path.join(rel_path, subfolder))

    # os.mknod("skeleton/main.py")
    # shutil.copyfile(
        # os.path.join(package, f"{os.path.basename(rel_path)}.py"),
        # os.path.join(repository, "solution", "main.py")
    # )
    print(
        os.path.join(package, f"{os.path.basename(rel_path)}.py"),
        os.path.join(repository, "solution", "main.py")
    )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
