#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

content = "Python,Spring"
pattern = re.compile("h.n")
print re.search(pattern, content).group()

m = re.match('the', 'food on the table')  # 匹配成功
print m
