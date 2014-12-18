# -*- coding: utf-8 -*-

import re
import textwrap

from nose import tools
from nose.tools import raises

from toggl2html.converter import detail


def test_read_file_01():
    """
    read_file()：引数に正しいファイルパスを指定したとき、ファイルの内容を返すことを確認する。
    """
    expected = textwrap.dedent("""\
        User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags,Amount ()
        ちぃといつ,7pairs@gmail.com,第4領域,娯楽,,クイズマジックアカデミー 天の学舎,いいえ,2014-06-23,10:00:00,2014-06-23,22:00:00,12:00:00,,
        ちぃといつ,7pairs@gmail.com,第3領域,生活,,睡眠,いいえ,2014-06-23,00:00:00,2014-06-23,08:00:00,08:00:00,,
    """)
    result = detail.read_file('./toggl2html/tests/in/test_read_file_01.csv')
    tools.assert_equal(expected, result)


@raises(getattr(__builtins__, 'FileNotFoundError', IOError))
def test_read_file_02():
    """
    read_file()：引数に存在しないファイルを指定したとき、FileNotFoundError(Python3.2のときはIOError)が送出されることを確認する。
    """
    detail.read_file('./toggl2html/tests/in/test_read_file_02.csv')


def test_parse_csv_01():
    """
    parse_csv()：引数として渡したCSVが辞書の配列に変換されることを確認する。
    """
    expected = [{
        'user': 'ちぃといつ',
        'email': '7pairs@gmail.com',
        'client': '第3領域',
        'project': '生活',
        'task': '',
        'description': '睡眠',
        'billable': 'いいえ',
        'start_date': '2014-06-23',
        'start_time': '00:00:00',
        'end_date': '2014-06-23',
        'end_time': '08:00:00',
        'duration': '08:00:00',
        'tags': '',
        'amount_()': '',
    }, {
        'user': 'ちぃといつ',
        'email': '7pairs@gmail.com',
        'client': '第4領域',
        'project': '娯楽',
        'task': '',
        'description': 'クイズマジックアカデミー 天の学舎',
        'billable': 'いいえ',
        'start_date': '2014-06-23',
        'start_time': '10:00:00',
        'end_date': '2014-06-23',
        'end_time': '22:00:00',
        'duration': '12:00:00',
        'tags': '',
        'amount_()': '',
    }]
    result = detail.parse_csv(textwrap.dedent("""\
        User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags,Amount ()
        ちぃといつ,7pairs@gmail.com,第4領域,娯楽,,クイズマジックアカデミー 天の学舎,いいえ,2014-06-23,10:00:00,2014-06-23,22:00:00,12:00:00,,
        ちぃといつ,7pairs@gmail.com,第3領域,生活,,睡眠,いいえ,2014-06-23,00:00:00,2014-06-23,08:00:00,08:00:00,,
    """))
    tools.assert_equal(expected, result)


def test_create_html_01():
    """
    create_html()：引数として渡した辞書の配列がHTMLに変換されることを確認する。
    """
    expected = textwrap.dedent("""\
        <!DOCTYPE html>
        <html lang="ja">
            <head>
                <meta charset="utf-8">
                <title>詳細レポート: 2014-06-23 - 2014-06-23</title>
                <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
            </head>
            <body>
                <h1>詳細レポート: 2014-06-23 - 2014-06-23</h1>
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

                            <tr>
                                <td>2014-06-23</td>
                                <td>睡眠<br>第3領域 - 生活</td>
                                <td>08:00:00<br>00:00:00 - 08:00:00</td>
                                <td>ちぃといつ</td>
                            </tr>

                            <tr>
                                <td>2014-06-23</td>
                                <td>クイズマジックアカデミー 天の学舎<br>第4領域 - 娯楽</td>
                                <td>12:00:00<br>10:00:00 - 22:00:00</td>
                                <td>ちぃといつ</td>
                            </tr>

                    </tbody>
                </table>
                <script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
                <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
            </body>
        </html>
    """)
    result = detail.create_html([{
        'user': 'ちぃといつ',
        'email': '7pairs@gmail.com',
        'client': '第3領域',
        'project': '生活',
        'task': '',
        'description': '睡眠',
        'billable': 'いいえ',
        'start_date': '2014-06-23',
        'start_time': '00:00:00',
        'end_date': '2014-06-23',
        'end_time': '08:00:00',
        'duration': '08:00:00',
        'tags': '',
        'amount_()': '',
    }, {
        'user': 'ちぃといつ',
        'email': '7pairs@gmail.com',
        'client': '第4領域',
        'project': '娯楽',
        'task': '',
        'description': 'クイズマジックアカデミー 天の学舎',
        'billable': 'いいえ',
        'start_date': '2014-06-23',
        'start_time': '10:00:00',
        'end_date': '2014-06-23',
        'end_time': '22:00:00',
        'duration': '12:00:00',
        'tags': '',
        'amount_()': '',
    }])
    tools.assert_equal(re.sub(r'[\s\n]', '', expected), re.sub(r'[\s\n]', '', result))


def test_create_html_02():
    """
    create_html()：引数として渡した辞書の配列がHTMLに変換されることを確認する。
    """
    expected = textwrap.dedent("""\
        <!DOCTYPE html>
        <html lang="ja">
            <head>
                <meta charset="utf-8">
                <title>詳細レポート: 2014-06-23 - 2014-06-25</title>
                <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
            </head>
            <body>
                <h1>詳細レポート: 2014-06-23 - 2014-06-25</h1>
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

                            <tr>
                                <td>2014-06-23</td>
                                <td>睡眠<br>第3領域 - 生活</td>
                                <td>08:00:00<br>00:00:00 - 08:00:00</td>
                                <td>ちぃといつ</td>
                            </tr>

                            <tr>
                                <td>2014-06-24</td>
                                <td>クイズマジックアカデミー 天の学舎<br>第4領域 - 娯楽</td>
                                <td>12:00:00<br>10:00:00 - 22:00:00</td>
                                <td>ちぃといつ</td>
                            </tr>

                            <tr>
                                <td>2014-06-25</td>
                                <td>toggl2html コーディング<br>第2領域 - GitHub</td>
                                <td>03:00:00<br>22:00:00 - 01:00:00</td>
                                <td>ちぃといつ</td>
                            </tr>

                    </tbody>
                </table>
                <script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
                <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
            </body>
        </html>
    """)
    result = detail.create_html([{
        'user': 'ちぃといつ',
        'email': '7pairs@gmail.com',
        'client': '第3領域',
        'project': '生活',
        'task': '',
        'description': '睡眠',
        'billable': 'いいえ',
        'start_date': '2014-06-23',
        'start_time': '00:00:00',
        'end_date': '2014-06-23',
        'end_time': '08:00:00',
        'duration': '08:00:00',
        'tags': '',
        'amount_()': '',
    }, {
        'user': 'ちぃといつ',
        'email': '7pairs@gmail.com',
        'client': '第4領域',
        'project': '娯楽',
        'task': '',
        'description': 'クイズマジックアカデミー 天の学舎',
        'billable': 'いいえ',
        'start_date': '2014-06-24',
        'start_time': '10:00:00',
        'end_date': '2014-06-24',
        'end_time': '22:00:00',
        'duration': '12:00:00',
        'tags': '',
        'amount_()': '',
    }, {
        'user': 'ちぃといつ',
        'email': '7pairs@gmail.com',
        'client': '第2領域',
        'project': 'GitHub',
        'task': '',
        'description': 'toggl2html コーディング',
        'billable': 'いいえ',
        'start_date': '2014-06-25',
        'start_time': '22:00:00',
        'end_date': '2014-06-26',
        'end_time': '01:00:00',
        'duration': '03:00:00',
        'tags': '',
        'amount_()': '',
    }])
    tools.assert_equal(re.sub(r'[\s\n]', '', expected), re.sub(r'[\s\n]', '', result))


def test_convert_snake_case_01():
    """
    convert_snake_case()：引数として指定された文字列がスネークケースに変換されることを確認する。
    """
    result = detail.convert_snake_case("cute and clever Elichika")
    tools.assert_equal("cute_and_clever_elichika", result)


def test_convert_snake_case_02():
    """
    convert_snake_case()：引数として指定された文字列が一単語の場合、すべて小文字に変換されることを確認する。
    """
    result = detail.convert_snake_case("Python")
    tools.assert_equal("python", result)


def test_convert_snake_case_03():
    """
    convert_snake_case()：引数として指定された文字列がすべて小文字で一単語の場合、変換後も同一の文字列であることを確認する。
    """
    result = detail.convert_snake_case("test")
    tools.assert_equal("test", result)
