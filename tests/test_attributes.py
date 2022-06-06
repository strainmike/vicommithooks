import os
import unittest

from vicommithooks import attributes

this_dir = os.path.dirname(os.path.realpath(__file__))


class TestAttributes(unittest.TestCase):
    def test_is_source_only(self):
        is_source_only = attributes.is_vi_source_only_from_path(
            os.path.join(this_dir, "test.vi")
        )
        assert is_source_only == False
