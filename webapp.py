#!/usr/bin/env python
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : jpp-birthday2013
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : GNU Lesser General Public License
# -----------------------------------------------------------------------------
# Creation : 13-Dec-2013
# Last mod : 13-Dec-2013
# -----------------------------------------------------------------------------
from flask import Flask, render_template, request, send_file, \
	send_from_directory, Response, abort, session, redirect, url_for, make_response
from flask.ext.assets import Environment

# from pymongo        import MongoClient
# from bson.json_util import dumps

app = Flask(__name__)
app.config.from_pyfile("settings.cfg")
Environment(app)

# -----------------------------------------------------------------------------
#
# Site pages
#
# -----------------------------------------------------------------------------
@app.route('/')
def index():
	response = make_response(render_template('home.html'))
	return response

# -----------------------------------------------------------------------------
#
# Main
#
# -----------------------------------------------------------------------------
if __name__ == '__main__':
	# run application
	app.run()

# EOF
