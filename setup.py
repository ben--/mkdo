import os
from setuptools import setup

source_dir = os.path.dirname(os.path.realpath(__file__))

setup(
    name='mkdo',
    version='0.1.0',

    description='Make Do - Manage Docker wrappers for build scripts',
    long_description='Make Do - Manage Docker wrappers for build scripts',

    url='https://github.com/ben--/mkdo',
    author='Ben Rogers',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='docker build',

    package_dir={'mkdo': os.path.join(source_dir, 'mkdo')},
    packages=['mkdo'],

    data_files = [
        ('scripts', [os.path.join(source_dir, 'scripts/setup.sh')]),
    ],

    entry_points = {
        'console_scripts': [
            'mkdo = mkdo:main',
        ],
    },
)
