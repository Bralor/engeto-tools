import xml.etree.ElementTree as te
import task_manager.text_processor as ttp


def test_if_select_boundaries_returns_expected_result():
    assert ttp.select_boundaries(["first line\\n", "---\\n", "third line\\n", "---\\n"], "---\\n") == [1,3]


def test_if_select_boundaries_returns_expected_data_type():
    result = ttp.select_boundaries(["first line\\n", "---\\n", "third line\\n", "---\\n"], "---\\n")
    assert isinstance(result, list)


def test_if_modify_indexes_returns_expected_result():
    assert ttp.modify_indexes([10, 12]) == (11, 12)


def test_if_modify_indexes_returns_expected_data_type():
    result = ttp.modify_indexes([10, 12])
    assert isinstance(result, tuple)


def test_if_remove_backticks_returns_expected_result():
    assert ttp.remove_backticks(["```", "a", "b"]) == ['a', 'b']


def test_if_remove_backticks_returns_expected_data_type():
    result = ttp.remove_backticks(["```", "a", "b"])
    assert isinstance(result, list)


def test_if_clean_newlines_strs_returns_expected_result():
    assert ttp.clean_newlines(["first line\n", "---\n", "third line\n", "---\n"]) == ['first line', '---', 'third line', '---']


def test_if_clean_newlines_returns_expected_data_type():
    result = ttp.clean_newlines(["first line\n", "---\n", "third line\n", "---\n"])
    assert isinstance(result, list)


def test_if_join_text_returns_expected_result():
    assert ttp.join_text(["a", "b", "c"]) == 'a\nb\nc'


def test_if_join_text_returns_expected_data_type():
    result = ttp.join_text(["a", "b", "c"])
    assert isinstance(result, str)


def test_if_replace_empty_strs_returns_expected_result():
    assert ttp.replace_empty_strs(["", ""]) == ['\n', '\n']


def test_if_replace_empty_strs_expected_data_type():
    result = ttp.replace_empty_strs(["", ""])
    assert isinstance(result, list)