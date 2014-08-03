#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os
import sys
import webapp2
import logging
import json

from google.appengine.ext import ndb
from google.appengine.api import mail

from google.appengine.ext.webapp import template

class PageHandler(webapp2.RequestHandler):

  def savedata(self):
    
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    
    #logging.info(self.request)
    my_json = json.loads(self.request.POST.get("datas"))
    logging.info(my_json["test"])