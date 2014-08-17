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

  def signin(self):
    
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    
    my_json = json.loads(self.request.POST.get("datas"))
    logging.info(my_json["email"])
    logging.info(my_json["password"])
    
  def signup(self):
    
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    
    #logging.info(self.request)
    my_json = json.loads(self.request.POST.get("datas"))
    logging.info(my_json["username"])
    logging.info(my_json["email"])
    logging.info(my_json["password"])
    logging.info(my_json["lastname"])