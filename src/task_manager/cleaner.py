
def select_names(exercises: list, lesson: dict) -> set:
    """
    Return an object of task names.

    :param exercises: a sequence of XML elements.
    :type exercises: list
    :return: an object with the names.
    :rtype: set
    """
    new_names = set()

    for exercise in exercises:
        solution = exercise.find("solution")
        path = solution.attrib.get("sourceDir", "nan_path")
        _, _, name , _ = path.split("/")
        new_names.add(lesson.get(name))

    return new_names
