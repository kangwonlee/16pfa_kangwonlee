import os
import subprocess

import nose
from nose.tools import *


def test_ex01_success():
    completed_process = subprocess.run(['python', os.path.join('ex01_print', 'ex01.py')], stdout=subprocess.PIPE)
    assert_true(completed_process)


def test_ex01_fail():
    completed_process = subprocess.run(['python', os.path.join('ex01_print', 'ex01_error.py')], stdout=subprocess.PIPE)
    assert_false(completed_process)


if __name__ == '__main__':
    # http://nose.readthedocs.io/en/latest/usage.html
    nose.main()
