import argparse
import os
import subprocess
import sys
import tempfile
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*')
    args, kwargs = parser.parse_known_args(argv)

    mapping = {}
    try:
        for file in args.files:
            with open(file, encoding='utf-8') as fd:
                content = fd.read()
            tmp_fd, path = tempfile.mkstemp(
                dir=os.path.dirname(file),
                prefix=os.path.basename(file),
                suffix='.py',
            )
            with open(tmp_fd, 'w', encoding='utf-8') as fd:
                fd.write(content.replace('\t', ' ' * 4))
            mapping[file] = (tmp_fd, path)

        inverse_mapping = {val[1]: key for key, val in mapping.items()}

        output = subprocess.run(
            [sys.executable, '-m', 'black', *inverse_mapping.keys(), *kwargs],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )
        ret = output.returncode
        for file, orig_file in inverse_mapping.items():
            with open(file, encoding='utf-8') as fd:
                content = fd.read()
            new_content = content.replace(' ' * 4, '\t')
            with open(orig_file, encoding='utf=8') as fd:
                old_content = fd.read()
            if old_content != new_content:
                ret = 1
                sys.stderr.write(f'reformatted {orig_file}\n')
                with open(orig_file, 'w', encoding='utf=8') as fd:
                    fd.write(new_content)

    finally:
        for tmp_fd, path in mapping.values():
            try:
                os.close(tmp_fd)
            except OSError:  # was already closed
                pass
            os.remove(path)

    stderr = output.stderr
    for file, orig_file in inverse_mapping.items():
        stderr = stderr.replace(file, orig_file)

    sys.stdout.write(output.stdout)
    sys.stderr.write(stderr)
    return ret


if __name__ == '__main__':
    sys.exit(main())
