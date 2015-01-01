# -*- coding: utf-8 -*-

"""
Tools for converting Toggl CSV to HTML

Usage:
toggl2html -i <input> -o <output>

Options:
-i <input>    input file path (CSV).
-o <output>   output file path (HTML).
-h --help     print this help message and exit.
-v --version  print the version number and exit.
"""
import os

from docopt import docopt

try:
    # setup.py実行後
    from toggl2html.converter import detail
    from toggl2html import __version__
except ImportError:
    # 未インストール状態での動作確認時
    from converter import detail
    dir_path = os.path.dirname(os.path.abspath(__file__))
    __version__ = [
        line.split('=')[1].strip().replace("'", '')
        for line in open(os.path.join(dir_path, '__init__.py'))
        if line.startswith('__version__ = ')
    ][0]


def main():
    """
    CSVファイルをHTMLに変換する。
    """
    # 引数を取得する
    args = docopt(__doc__, version=__version__)

    # CSVファイルをHTMLに変換する
    detail.execute(args['-i'], args['-o'])


if __name__ == '__main__':
    main()
