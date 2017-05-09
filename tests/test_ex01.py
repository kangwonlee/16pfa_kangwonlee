import os
import subprocess

import nose
import nose.tools as nt


def test_ex01_success():
    completed_process = subprocess.run(['python', os.path.join('ex01_print', 'ex01.py')], stdout=subprocess.PIPE)
    nt.assert_equal(0, completed_process.returncode)
    nt.assert_true(completed_process.stdout)


def test_all_scripts_recursively():
    for full_path, dir_list, file_list in os.walk(os.getcwd()):
        if '.git' not in full_path:
            for file_name in file_list:
                if file_name.endswith('.py'):
                    process_python_script(file_name, full_path)


def process_python_script(file_name, full_path):
    script_full_path = os.path.join(full_path, file_name)
    print(script_full_path)
    with open(script_full_path, 'rt', encoding='utf8') as input_file:
        script_text = input_file.read()

    # skip if
    if 'argv' not in script_text:
        completed_process = subprocess.run(['python', script_full_path], stdout=subprocess.PIPE)
        nt.assert_equal(0, completed_process.returncode, msg=script_full_path)
        # true if script output is not empty or print is not in script
        nt.assert_true(completed_process.stdout or ('print' not in script_text), msg=script_full_path)


if __name__ == '__main__':
    # http://nose.readthedocs.io/en/latest/usage.html
    nose.main()
