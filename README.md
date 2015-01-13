# toggl2html

[![Build Status](https://travis-ci.org/7pairs/toggl2html.svg?branch=master)](https://travis-ci.org/7pairs/toggl2html)
[![Coverage Status](https://img.shields.io/coveralls/7pairs/toggl2html.svg)](https://coveralls.io/r/7pairs/toggl2html?branch=master)

## 概要

TogglからダウンロードしたCSVファイルをHTMLの表に変換するツールです。日本語を含むログをビジュアライズする手段が公式には存在しないため（TogglからダウンロードできるPDFは日本語が化けてしまう）このツールを作りました。

## バージョン

Python3.4での動作を確認しています。また、3.3でもユニットテストを行っていますので、おそらくこのバージョンでも動作するものと思われます。なお、Python2系には対応しておりません。ご了承ください。

## インストール

同梱の `setup.py` を実行してください。

```
python setup.py install
```

pipを導入している方は、GitHubから直接インストールすることもできます。

```
pip install git+https://github.com/7pairs/toggl2html.git
```

## 実行方法

入力ファイル（CSV形式）、出力ファイル（HTML形式）を指定して実行してください。

```
toggl2html -i <input-file-path> -o <output-file-path>
```
