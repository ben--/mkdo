"""mkdo - create and manage do/* scripts"""

import os
import sys


def main():
    """Main mkdo entrypoint"""
    sys.stderr.write('running')
    os.mkdir('do')
    with open('do/build', 'w'):
        pass
    os.chmod('do/build', 0o555)
