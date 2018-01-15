#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
__date__ = '2018/1/14'

import requests

url_response = requests.get("http://zkeeer.space")
print url_response.status_code, url_response.text
