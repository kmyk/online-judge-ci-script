import platform
import textwrap
import unittest
from typing import *

import onlinejudge_verify.languages.cplusplus as cplusplus
import tests.utils


class TestCPlusPlusListDependencies(unittest.TestCase):
    """TestCPlusPlusListDependencies has unit tests for the feature to list dependencies of C++ files.
    """
    def test_success(self) -> None:
        """
        Test the test test files

        Args:
            self: (todo): write your description
        """
        files = {
            'main.cpp': textwrap.dedent("""\
                #include "included.hpp"
                """).encode(),
            'included.hpp': textwrap.dedent("""\
                int main() {}
                """).encode(),
        }

        with tests.utils.load_files(files) as tempdir:
            with tests.utils.chdir(tempdir):
                expected = sorted([tempdir / 'main.cpp', tempdir / 'included.hpp'])
                actual = sorted(cplusplus.CPlusPlusLanguage().list_dependencies(tempdir / 'main.cpp', basedir=tempdir))
                self.assertEqual(actual, expected)

    @unittest.skipIf(platform.system() == 'Windows', "The path separator should be '/' for this test.")
    def test_failure_with_backslash(self) -> None:
        """
        Test for backslash

        Args:
            self: (todo): write your description
        """
        files = {
            'main.cpp': textwrap.dedent("""\
                #include ".\\included.hpp"
                """).encode(),
            'included.hpp': textwrap.dedent("""\
                int main() {}
                """).encode(),
        }

        with tests.utils.load_files(files={}) as tempdir:
            with tests.utils.chdir(tempdir):
                self.assertRaises(Exception, lambda: cplusplus.CPlusPlusLanguage().list_dependencies(tempdir / 'main.cpp', basedir=tempdir))

    @unittest.skipIf(platform.system() in ('Windows', 'Darwin'), "The filesystem should be case-sensitive for this test.")
    def test_failure_with_case_insensitive(self) -> None:
        """
        Create a case that the test case of the test case.

        Args:
            self: (todo): write your description
        """
        files = {
            'main.cpp': textwrap.dedent("""\
                #include "INCLUDED.HPP"
                """).encode(),
            'included.hpp': textwrap.dedent("""\
                int main() {}
                """).encode(),
        }

        with tests.utils.load_files(files={}) as tempdir:
            with tests.utils.chdir(tempdir):
                self.assertRaises(Exception, lambda: cplusplus.CPlusPlusLanguage().list_dependencies(tempdir / 'main.cpp', basedir=tempdir))
