# -*- coding: utf-8 -*-

import sys

try:
    # setup.py実行後
    from toggl2html.converter import detail
except ImportError:
    # 未インストール状態での動作確認時
    from converter import detail


def main():
    """
    CSVファイルをHTMLに変換する。
    """
    # 引数をチェックする
    if len(sys.argv) != 3:
        print('Usage: toggl2html <input-file-path> <output-file-path>')
        quit()

    # 変換を実行する
    detail.execute(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
