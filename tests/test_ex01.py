import os
import subprocess
from nose.tools import *
# http://nose.readthedocs.io/en/latest/usage.html
# to run nose.main()
import nose


def test_ex01_success():
    completed_process = subprocess.run(['python', os.path.join(os.pardir, 'ex01_print', 'ex01.py')], stdout=subprocess.PIPE)
    assert_true(completed_process)


def test_ex01_fail():
    completed_process = subprocess.run(['python', os.path.join(os.pardir, 'ex01_print', 'ex01.py')], stdout=subprocess.PIPE)
    assert_false(completed_process)


if __name__ == '__main__':
    # http://nose.readthedocs.io/en/latest/usage.html
    nose.main()
