# -*- coding: utf-8 -*-


# 生成するHTMLのテンプレート
HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <title>詳細レポート: {{ start_date }} - {{ end_date }}</title>
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
    </head>
    <body>
        <h1>詳細レポート: {{ start_date }} - {{ end_date }}</h1>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>日付</th>
                    <th>説明</th>
                    <th>期間</th>
                    <th>ユーザー</th>
                </tr>
            </thead>
            <tbody>
                {% for line in lines %}
                    <tr>
                        <td>{{ line.start_date }}</td>
                        <td>{{ line.description }}<br>{{ line.client }} - {{ line.project }}</td>
                        <td>{{ line.duration }}<br>{{ start_time }} - {{ end_time }}</td>
                        <td>{{ line.user }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
    </body>
</html>
"""


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
    for line in reversed(lines[1:]):
        elements = line.split(',')
        ret_val.append({convert_snake_case(captions[i]): element for i, element in enumerate(elements)})

    # 解析結果を返す
    return ret_val


def convert_snake_case(target):
    """
    文字列をスネークケースに変換する。

    :param target: 変換対象の文字列
    :type target: str
    :return: 変換後の文字列
    :rtype: str
    """
    # 文字列をスネークケースに変換する
    return target.lower().replace(' ', '_')
