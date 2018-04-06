#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: ministry

try:
    from flask import Flask
    app = Flask(__name__, template_folder="views")
except ImportError as e:
    raise e



try:
    app.run(host="0.0.0.0", port="80", debug="True")
except BaseException as ideentifier:
    raise e