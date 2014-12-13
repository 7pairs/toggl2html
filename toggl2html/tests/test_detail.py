# -*- coding: utf-8 -*-

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
        'amount_()': ''
    }, {
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
        'amount_()': ''
    }]
    result = detail.parse_csv(textwrap.dedent("""\
        User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags,Amount ()
        ちぃといつ,7pairs@gmail.com,第4領域,娯楽,,クイズマジックアカデミー 天の学舎,いいえ,2014-06-23,10:00:00,2014-06-23,22:00:00,12:00:00,,
        ちぃといつ,7pairs@gmail.com,第3領域,生活,,睡眠,いいえ,2014-06-23,00:00:00,2014-06-23,08:00:00,08:00:00,,
    """))
    tools.assert_equal(expected, result)


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
