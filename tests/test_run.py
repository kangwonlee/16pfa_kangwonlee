import os
import subprocess

import nose
import nose.tools as nt


def test_ex01():
    completed_process = subprocess.run(['python', os.path.join('ex01_print', 'ex01.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex02():
    completed_process = subprocess.run(['python', os.path.join('ex02_comment', 'ex02.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex03():
    completed_process = subprocess.run(['python', os.path.join('ex03_calculation', 'ex03.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex04():
    completed_process = subprocess.run(['python', os.path.join('ex04_variables', 'ex04.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex05():
    completed_process = subprocess.run(['python', os.path.join('ex05_string_interpolation', 'ex05.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex06():
    completed_process = subprocess.run(['python', os.path.join('ex06_string_operation', 'ex06.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex07():
    completed_process = subprocess.run(['python', os.path.join('ex07_string_operation', 'ex07.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex07_python3():
    completed_process = subprocess.run(['python', os.path.join('ex07_string_operation', 'ex07_python3.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex08():
    completed_process = subprocess.run(['python', os.path.join('ex08_formatter_string', 'ex08.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex09():
    completed_process = subprocess.run(['python', os.path.join('ex09_multiline', 'ex09.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex10():
    completed_process = subprocess.run(['python', os.path.join('ex10_escape_sequence', 'ex10.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex19():
    completed_process = subprocess.run(['python', os.path.join('ex19_arguments', 'ex19.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex21():
    completed_process = subprocess.run(['python', os.path.join('ex21_return', 'ex21.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex24():
    completed_process = subprocess.run(['python', os.path.join('ex24_summary', 'ex24.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex25():
    completed_process = subprocess.run(['python', os.path.join('ex25_module', 'ex25.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)


def test_run_ex25():
    completed_process = subprocess.run(['python', os.path.join('ex25_module', 'run_ex25.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex28():
    completed_process = subprocess.run(['python', os.path.join('ex28_boolean_operations', 'ex28.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex29():
    completed_process = subprocess.run(['python', os.path.join('ex29_if', 'ex29.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex30():
    completed_process = subprocess.run(['python', os.path.join('ex30_if_elif_else', 'ex30.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex32():
    completed_process = subprocess.run(['python', os.path.join('ex32_for_list', 'ex32.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex33():
    completed_process = subprocess.run(['python', os.path.join('ex33_while', 'ex33.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex34():
    completed_process = subprocess.run(['python', os.path.join('ex34_list_index', 'ex34.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_recursion_example():
    completed_process = subprocess.run(['python', os.path.join('ex35_structural_programming', 'recursion_example.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex38():
    completed_process = subprocess.run(['python', os.path.join('ex38_list', 'ex38.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex39():
    completed_process = subprocess.run(['python', os.path.join('ex39_dict_hashmap', 'ex39.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_ex39_test():
    completed_process = subprocess.run(['python', os.path.join('ex39_dict_hashmap', 'ex39_test.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_hashmap():
    completed_process = subprocess.run(['python', os.path.join('ex39_dict_hashmap', 'hashmap.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)


def test_ex40():
    completed_process = subprocess.run(['python', os.path.join('ex40_dict_module_class', 'ex40.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_mystuff():
    completed_process = subprocess.run(['python', os.path.join('ex40_dict_module_class', 'mystuff.py')],
                                       stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)


def test_game():
    completed_process = subprocess.run(['python', os.path.join('ex47_nose_tests', 'game.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)


if __name__ == '__main__':
    # http://nose.readthedocs.io/en/latest/usage.html
    nose.main()
