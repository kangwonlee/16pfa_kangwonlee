import os
import subprocess

import nose
import nose.tools as nt


def test_ex01_success():
    completed_process = subprocess.run(['python', os.path.join('ex01_print', 'ex01.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex01_error():
    completed_process = subprocess.run(['python', os.path.join('ex01_print', 'ex01_error.py')], stdout=subprocess.PIPE)
    nt.assert_not_equal(0, completed_process.returncode)


if __name__ == '__main__':
    # http://nose.readthedocs.io/en/latest/usage.html
    nose.main()
