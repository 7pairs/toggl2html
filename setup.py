# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from toggl2html import __version__


setup(
    name='toggl2html',
    version=__version__,
    description='Tools for converting Toggl CSV to HTML',
    author='Jun-ya HASEBA',
    author_email='7pairs@gmail.com',
    url='http://seven-pairs.hatenablog.jp/',
    packages=find_packages(),
    install_requires=['Jinja2', 'docopt'],
    entry_points="""\
    [console_scripts]
    toggl2html = toggl2html.toggl2html:main
    """
)
