import argparse
import sys
from typing import Dict

from utilities import count_bytes, count_characters, count_lines, count_words

"""The ccwc.py module is responsible for handling the user interactions"""

parser = argparse.ArgumentParser(
    prog="ccwc.py",
    usage="%(prog)s [options] FILE [FILE...]",
    description="Print newline, word and byte for each file",
)
parser.add_argument(
    "files",
    metavar="FILE",
    default="",
    type=str,
    nargs="*",
    help="take a file or a list of files",
)
parser.add_argument(
    "-l",
    "--line",
    default=False,
    action="store_true",
    help="print the line counts",
)
parser.add_argument(
    "-c",
    "--byte",
    default=False,
    action="store_true",
    help="print the byte counts",
)
parser.add_argument(
    "-m",
    "--char",
    default=False,
    action="store_true",
    help="print the character counts",
)
parser.add_argument(
    "-w",
    "--word",
    default=False,
    action="store_true",
    help="print the word counts",
)


def wrapper(func, byteObject: bytes, key: str) -> None:
    global message
    c_obj = func(byteObject)
    message += f"{c_obj} "
    files_metric_summary.setdefault(key, 0)
    files_metric_summary.update({key: files_metric_summary.get(key) + c_obj})


def generate_file_metric(byteObject: bytes):
    if not any([args.line, args.word, args.byte, args.char]):
        wrapper(count_lines, byteObject, "lines")
        wrapper(count_words, byteObject, "words")
        wrapper(count_bytes, byteObject, "bytes")
    else:
        if args.line:
            wrapper(count_lines, byteObject, "lines")

        if args.word:
            wrapper(count_words, byteObject, "words")

        if args.byte:
            wrapper(count_bytes, byteObject, "bytes")

        if args.char:
            wrapper(count_characters, byteObject, "chars")


if __name__ == "__main__":
    args = parser.parse_args()

    message: str = ""
    files_metric_summary: Dict[str, int] = {}

    for file in args.files:
        with open(file, "rb") as fd:
            generate_file_metric(fd.read())

        message += f"{file}"
        print(message)
        message = ""

    # If no file is passed read stdin
    if not args.files:
        generate_file_metric(sys.stdin.buffer.read())
        print(message)

    # If provided files are more than one show total
    if len(args.files) > 1:
        print(*files_metric_summary.values(), "total")
