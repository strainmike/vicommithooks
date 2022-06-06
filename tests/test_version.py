import os
import unittest

from vicommithooks import version

this_dir = os.path.dirname(os.path.realpath(__file__))


class TestVersion(unittest.TestCase):
    def test_get_version(self):
        vi_version = version.get_version_from_path(os.path.join(this_dir, "test.vi"))
        test_version = version.LVVersion(
            {"major": 20, "minor": 0, "bugfix": 0, "stage": 4}
        )
        assert test_version == vi_version

    def test_less_than(self):
        lower_version = version.LVVersion(
            {"major": 20, "minor": 0, "bugfix": 0, "stage": 0}
        )
        higher_version = version.LVVersion(
            {"major": 21, "minor": 0, "bugfix": 0, "stage": 0}
        )
        assert lower_version < higher_version
        lower_version = version.LVVersion(
            {"major": 21, "minor": 0, "bugfix": 0, "stage": 0}
        )
        higher_version = version.LVVersion(
            {"major": 21, "minor": 1, "bugfix": 0, "stage": 0}
        )
        assert lower_version < higher_version
        lower_version = version.LVVersion(
            {"major": 21, "minor": 0, "bugfix": 0, "stage": 0}
        )
        higher_version = version.LVVersion(
            {"major": 21, "minor": 0, "bugfix": 0, "stage": 0}
        )
        assert lower_version < higher_version
        lower_version = version.LVVersion(
            {"major": 21, "minor": 0, "bugfix": 0, "stage": 0}
        )
        higher_version = version.LVVersion(
            {"major": 21, "minor": 0, "bugfix": 1, "stage": 0}
        )
        assert lower_version < higher_version
        lower_version = version.LVVersion(
            {"major": 21, "minor": 0, "bugfix": 0, "stage": 0}
        )
        higher_version = version.LVVersion(
            {"major": 21, "minor": 0, "bugfix": 0, "stage": 1}
        )
        assert lower_version < higher_version
        lower_version = version.LVVersion(
            {"major": 0, "minor": 0, "bugfix": 0, "stage": 0}
        )
        higher_version = version.LVVersion(
            {"major": 20, "minor": 0, "bugfix": 0, "stage": 0}
        )
        assert lower_version < higher_version
