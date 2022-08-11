def process_text(text: list) -> str:
    """
    Return the processed text.

    :Example:
    >>> process_text(
    ...    ["first line\\n", "---\\n",  "```\\n", "```\\n",
    ...    "third line\\n", "---\\n"]
    ... )
    'third line'
    """
    bounds = select_boundaries(text, "---\n")
    start, stop = modify_indexes(bounds)
    cleaned_txt = remove_backticks(
        clean_newlines(text[start: stop]),
        2
    )
    return join_text(replace_empty_strs(cleaned_txt))


def select_boundaries(content: list, signal: str) -> list:
    """
    Return the beginning and the final index of the text.

    :param content: a content of README.md file.
    :type content: list
    :param signal: a delimiter from the text.
    :type signal: str
    :return: a pair of first and last indexes.
    :rtype: list

    :Example:
    >>> select_boundaries(
    ...     ["first line\\n", "---\\n", "third line\\n", "---\\n"], "---\\n"
    ... )
    [1, 3]
    """
    return [
        index
        for index, item in enumerate(content)
        if item == signal
    ]


def modify_indexes(indexes: list) -> tuple:
    """
    Modify and return the final numbers of possible boundaries.

    :param indexes: a first and last indexes of the text.
    :type indexes: list
    :return: a modified numbers of indexes.
    :rtype: tuple

    :Example:
    >>> modify_indexes([11, 15])
    (12, 15)
    """
    return indexes[0] + 1, indexes[-1]


def remove_backticks(seq: list, times: int = 1) -> list:
    """
    Remove the backticks from the given sequence.

    :param seq: a sequence of words.
    :type seq: list
    :param times: a number of removing steps.
    :type times: int
    :return: a cleaned object without backticks.
    :rtype: list

    :Example:
    >>> remove_backticks(["```", "a", "b"])
    ['a', 'b']
    >>> remove_backticks(["```", "a","```", "b"], 2)
    ['a', 'b']
    """
    for _ in range(times):
        try:
            seq.remove("```")

        except ValueError:
            break

    return seq


def clean_newlines(seq: list) -> list:
    """
    Return the list without a pending newline chars.

    :param seq: a sequence of words.
    :type seq: list
    :return: a cleaned object without empty strings.
    :rtype: list

    :Example:
    >>> clean_newlines(["first line\\n", "---\\n", "third line\\n", "---\\n"])
    ['first line', '---', 'third line', '---']
    """
    return [
        item.strip()
        for item in seq
    ]


def join_text(seq: list) -> str:
    """
    Join the text with proper newlines.

    :param seq: a sequence of words.
    :type seq: list
    :return: a merged object within a single string.
    :rtype: str

    :Example:
    >>> join_text(["a", "b", "c"])
    'a\\nb\\nc'
    """
    return "\n".join(seq)


def replace_empty_strs(seq: list) -> list:
    """
    Add a newline where should be and return the complete list.

    :param seq: a sequence of words.
    :type seq: list
    :return: a merged object within a single string.
    :rtype: list

    :Example:
    >>> replace_empty_strs(["", ""])
    ['\\n', '\\n']
    """
    return [
        "\n" if not item
        else item
        for item in seq
    ]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
