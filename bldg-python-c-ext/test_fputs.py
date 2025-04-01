"""
Test our Python C function: `fputs`
"""

import fputs


def test_copy_data():
    content_to_copy = "Real Python!"
    bytes_copied = fputs.fputs(content_to_copy, "test_write.txt")

    with open("test_write.txt", "r") as f:
        content_copied = f.read()

    assert bytes_copied == len(content_to_copy)
    assert content_copied == content_to_copy
