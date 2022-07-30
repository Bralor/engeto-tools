import xml.etree.ElementTree


def get_xml_root(filename: str) -> xml.etree.ElementTree.ElementTree:
    """
    Get the root of the XML structure.

    :param filename: a name of the xml file.
    :type filename: str
    :return: an object with the content of the xml.
    :rtype: xml.etree.ElementTree.Element

    :Example:
    >>> isinstance(
    ...     get_xml_root("srcTests/tests/foo.xml"),
    ...     xml.etree.ElementTree.ElementTree
    ... )
    True
    """
    return xml.etree.ElementTree.parse(filename)


def set_xml_attr(**kwargs):
    """
    Returns a dictionary object with the given parameters.

    :Example:
    >>> print(set_xml_attr(name="foo", surname="bar"))
    {'name': 'foo', 'surname': 'bar'}
    """
    return {
        key: val
        for key, val in kwargs.items()
    }


if __name__ == "__main__":
    import doctest
    doctest.testmod()
