# -*- coding: utf-8 -*-

from jinja2 import Template


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
                        <td>{{ line.duration }}<br>{{ line.start_time }} - {{ line.end_time }}</td>
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


def execute(in_file, out_file):
    """
    CSVファイルをHTMLに変換する。

    :param in_file: CSVファイルのパス
    :type in_file: str
    :param out_file: HTMLのパス
    :type out_file: str
    """
    # CSVファイルをHTMLに変換する
    csv = read_file(in_file)
    data = parse_csv(csv)
    html = create_html(data)
    with open(out_file, 'w') as f:
        f.write(html)


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
        ret_val.append({convert_snake_case(captions[i]): element for i, element in enumerate(elements)})

    # 解析結果を返す
    return ret_val


def create_html(param):
    """
    タイムトラッキングの辞書の配列を解析し、その内容をHTMLとして返す。

    :param param: CSV解析結果の辞書が格納された配列
    :type param: List[Dict[str, str]]
    :return: 解析結果のHTML
    :rtype: str
    """
    # テンプレートを構築する
    template = Template(HTML_TEMPLATE)

    # 開始日／終了日を取得する
    start_date = param[0]['start_date']
    end_date = param[-1]['start_date']

    # レンダリング結果を返す
    return template.render({
        'start_date': start_date,
        'end_date': end_date,
        'lines': param,
    })


def save_file(file_path, data):
    """
    文字列をファイルに保存する。
    :param file_path: ファイルパス
    :type file_path: str
    :param data: 保存する文字列
    :type data: str
    """
    # 文字列をファイルに保存する
    with open(file_path, 'a') as f:
        f.write(data)


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
