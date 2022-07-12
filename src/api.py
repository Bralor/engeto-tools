import os
import sys

from src.processor import task_processor


def main():
    """
    :Example:
    >>> main(sys.argv[1], sys.argv[2])
    Running task checks..
    """
    print("Running task checks..") if len(sys.argv) == 2 else print("Nope!")
    task_processor()


if __name__ == "__main__":
    main()
