import flask
from flask import request, jsonify
import requests
from bs4 import BeautifulSoup

app = flask.Flask(__name__)

#url = 'https://chrisvoo1992.pythonanywhere.com/2013'
#r = requests.get(url)
@app.route('/<year>')
def show(year):
    url = 'https://chrisvoo1992.pythonanywhere.com/' + str(year)
    r = requests.get(url)
    li = list(r)
    return li


if (__name__) == '__main__':
    app.run(debug = True)