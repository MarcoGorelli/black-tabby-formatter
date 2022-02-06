import os
import subprocess


def test_main(tmpdir):
    content = 'if  True:\n    pass'
    file = os.path.join(tmpdir, 'tmpfile.py')
    with open(file, 'w') as fd:
        fd.write(content)
    output = subprocess.run(
        [
            'python', '-m', 'black_tabby_formatter',
            file,
        ], universal_newlines=True, capture_output=True,
    )
    with open(file) as fd:
        newcontent = fd.read()

    assert newcontent == 'if True:\n\tpass\n'
    assert 'reformatted' in output.stderr
    assert output.returncode == 1


def test_main_noop(tmpdir):
    content = 'if True:\n\tpass\n'
    file = os.path.join(tmpdir, 'tmpfile.py')
    with open(file, 'w') as fd:
        fd.write(content)
    output = subprocess.run(
        [
            'python', '-m', 'black_tabby_formatter',
            file,
        ], universal_newlines=True, capture_output=True,
    )
    with open(file) as fd:
        newcontent = fd.read()

    assert newcontent == content
    assert 'unchanged' in output.stderr
    assert output.returncode == 0


def test_main_no_black_change(tmpdir):
    content = 'if True:\n    pass\n'
    file = os.path.join(tmpdir, 'tmpfile.py')
    with open(file, 'w') as fd:
        fd.write(content)
    output = subprocess.run(
        [
            'python', '-m', 'black_tabby_formatter',
            file,
        ], universal_newlines=True, capture_output=True,
    )
    with open(file) as fd:
        newcontent = fd.read()

    assert newcontent == 'if True:\n\tpass\n'
    assert 'reformatted' in output.stderr
    assert output.returncode == 1


def test_main_multiple_files(tmpdir):
    content1 = 'if True :\n    pass\n'
    file1 = os.path.join(tmpdir, 'tmpfile1.py')
    with open(file1, 'w') as fd:
        fd.write(content1)
    content2 = 'if False:\n    pass\n'
    file2 = os.path.join(tmpdir, 'tmpfile2.py')
    with open(file2, 'w') as fd:
        fd.write(content2)
    output = subprocess.run(
        [
            'python', '-m', 'black_tabby_formatter',
            file1, file2,
        ], universal_newlines=True, capture_output=True,
    )
    with open(file1) as fd:
        newcontent1 = fd.read()
    with open(file2) as fd:
        newcontent2 = fd.read()

    assert newcontent1 == 'if True:\n\tpass\n'
    assert newcontent2 == 'if False:\n\tpass\n'
    assert 'reformatted' in output.stderr
    assert output.returncode == 1
