# -*- coding: utf-8 -*-
"""Adds Textile markup support to Lektor.

date: 2018-02-20

Using:
  In  model file (page.ini) add (example):
    [fields.body]
    label = Body
    type = textile


depends:
  textile

"""
__version__ = '0.1'
__author__ = 'Viktor Semenyuk <svafn1@gmail.com>'

from lektor.pluginsystem import Plugin
from lektor.types import Type
import textile


def textile_to_html(text):
    # convert Textile markup to html
    out = textile.textile(text=text)
    return out


class HTML(object):
    # Lektor from escaping HTML tags.

    def __init__(self, html):
        self.html = html

    def __html__(self):
        return self.html


class TextileType(Type):
    widget = 'multiline-text'

    def value_from_raw(self, raw):
        return HTML(textile_to_html(raw.value or u''))


class TextilePlugin(Plugin):
    name = u'lektor-textile'
    description = u'Adds Textile markup support to Lektor (as standalone files).'

    def on_setup_env(self, **extra):
        self.env.add_type(TextileType)
