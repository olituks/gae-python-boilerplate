#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os
import re
import webapp2
import logging

from webapp2 import Route

DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

# webapp2 config
config = {
	'webapp2_extras.sessions': {
	    'secret_key': 'wIDjEesObzp5nonpRHDzSp40aba7STuqC6ZRY'
	}
}

if 'lib' not in sys.path:
  sys.path[0:0] = ['lib']

# Map URLs to handlers
routes = [
  # home Page.
  Route(r'/savedata', handler='handlers.PageHandler:savedata', name='savedata')
]

app = webapp2.WSGIApplication(routes, debug=DEBUG, config=config)