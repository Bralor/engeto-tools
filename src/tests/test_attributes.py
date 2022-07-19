import xml.etree.ElementTree as te

from src.task_manager.attributes import update_exercise


def test_update_exercise_with_proper_elements():
    tree = te.parse("src/tests/bar.xml")
    root = tree.getroot()
    exercises = [exercise for exercise in root.iter("exercise")]
    update_exercise(
        exercises[0], "XXXXX", "sourceDir", "skeleton", "solution"
    )
    assert exercises[0].find("skeleton").attrib["sourceDir"] == "XXXXX"
