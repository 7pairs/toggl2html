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
