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
        'User': 'ちぃといつ',
        'Email': '7pairs@gmail.com',
        'Client': '第4領域',
        'Project': '娯楽',
        'Task': '',
        'Description': 'クイズマジックアカデミー 天の学舎',
        'Billable': 'いいえ',
        'Start date': '2014-06-23',
        'Start time': '10:00:00',
        'End date': '2014-06-23',
        'End time': '22:00:00',
        'Duration': '12:00:00',
        'Tags': '',
        'Amount ()': ''
    }, {
        'User': 'ちぃといつ',
        'Email': '7pairs@gmail.com',
        'Client': '第3領域',
        'Project': '生活',
        'Task': '',
        'Description': '睡眠',
        'Billable': 'いいえ',
        'Start date': '2014-06-23',
        'Start time': '00:00:00',
        'End date': '2014-06-23',
        'End time': '08:00:00',
        'Duration': '08:00:00',
        'Tags': '',
        'Amount ()': ''
    }]
    result = detail.parse_csv(textwrap.dedent("""\
        User,Email,Client,Project,Task,Description,Billable,Start date,Start time,End date,End time,Duration,Tags,Amount ()
        ちぃといつ,7pairs@gmail.com,第4領域,娯楽,,クイズマジックアカデミー 天の学舎,いいえ,2014-06-23,10:00:00,2014-06-23,22:00:00,12:00:00,,
        ちぃといつ,7pairs@gmail.com,第3領域,生活,,睡眠,いいえ,2014-06-23,00:00:00,2014-06-23,08:00:00,08:00:00,,
    """))
    tools.assert_equal(expected, result)
