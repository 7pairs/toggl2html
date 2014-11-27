# -*- coding: utf-8 -*-


def read_file(file_path):
    """
    ファイルを読み込み、内容を文字列として返す。

    :param file_path: ファイルのパス
    :type file_path: str
    :return: ファイルの内容
    :rtype: str
    """
    # 指定されたファイルの内容を返す
    with open(file_path) as f:
        return f.read()
