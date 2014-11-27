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


def parse_csv(csv):
    """
    CSVを解析し、その内容を辞書として返す。

    :param csv: CSV文字列
    :type csv: str
    :return: 解析結果の辞書が格納された配列
    :rtype: List[Dict[str, str]]
    """
    # 戻り値用の配列
    ret_val = []

    # 見出しを解析する
    lines = csv.splitlines()
    captions = lines[0].split(',')

    # 明細行を解析する
    for line in lines[1:]:
        elements = line.split(',')
        ret_val.append({captions[i]: element for i, element in enumerate(elements)})

    # 解析結果を返す
    return ret_val
