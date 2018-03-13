# -*- coding: utf-8 -*-
from .parser import parse
from .lexer import lex
from .builder import build
from .objects import map, load
from .ext.lua import LuaBlockPlugin

__all__ = ['parse', 'lex', 'build', 'map', 'load']

__title__ = 'crossplane'
__summary__ = 'Reliable and fast NGINX configuration file parser.'
__url__ = 'https://github.com/nginxinc/crossplane'

__version__ = '0.2.0'

__author__ = 'Arie van Luttikhuizen'
__email__ = 'aluttik@gmail.com'

__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2017 NGINX, Inc.'

default_enabled_extensions = [LuaBlockPlugin()]
for extension in default_enabled_extensions:
    extension.register_extension()
