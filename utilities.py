import re


def count_bytes(byteObject: bytes) -> int:
    return len(byteObject)


def count_words(byteObject: bytes) -> int:
    return len(
        [word for word in re.split("\s", byteObject.decode()) if word != ""]
    )


def count_lines(byteObject: bytes, i: int = 0) -> int:
    for ch in byteObject.decode():
        if ch == "\n":
            i += 1
    return i


def count_characters(byteObject: bytes) -> int:
    return len(byteObject.decode())
