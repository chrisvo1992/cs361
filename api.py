import flask
from flask import request, jsonify
import requests
from bs4 import BeautifulSoup
import pandas as pd

mydict = {
    '2021' : [1,2,3,],
    '2020' : [ 2434,465,]
}
print(mydict['2020'])
app = flask.Flask(__name__)
#app.config["DEBUG"] = True
#url = 'https://www.boxofficemojo.com/year/2015/'
#table_id = 'a-text-left mojo-field-type-release mojo-cell-wide'

@app.route('/<year>')
def movies(year):
    list = []
    mov = ''
    url = 'https://www.boxofficemojo.com/year/' + str(year) + '/'
    table_id = 'a-text-left mojo-field-type-release mojo-cell-wide'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find_all('td', attrs={'class': table_id})
    for item in table:
        item = str(item)
        mov = item[135:-9]
        index = 0
        for i in mov:
            if i == '>':
                mov = mov[index + 1:]
                x = mov.find('<')
                if x > 0:
                    mov = mov[:x]
                list.append(mov)
                break
            else:
                index += 1

    return jsonify(list)

#@app.route('/', methods=['GET'])
#def home():
#    return '''<h1>Distant Reading Archive</h1>
#<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
#@app.route('/<year>', methods=['GET'])
#def api_all(year):
#    return jsonify(movies[year])

#list = []
#mov = ''
#r = requests.get(url)

#soup = BeautifulSoup(r.text, 'html.parser')
#table = soup.find_all('td', attrs={'class': table_id})

#for item in table:
#    item = str(item)
#    mov = item[135:-9]
#    index = 0
#    for i in mov:
 #       if i == '>':
  #          mov = mov[index+1:]
   #         x = mov.find('<')
    #        if x > 0 :
     #           mov = mov[:x]
      #      list.append(mov)
       #     break
        #else:
         #   index +=1

#table = table[:-9]
#print(table)
#for i in reversed(table):
#    if i == '>':
#        list.append(mov[::-1])
#        break
#    else:
#        mov = mov + i

#print(list)
#print(soup.prettify())
#test = []
#table = soup.find('id', attrs={})

#@app.route('/show', methods=['GET'])
#def api_all():
#    return jsonify(list)

if (__name__) == '__main__':
    app.run(debug = True)
mydict = {
    '2021' : [1,2,3,],
    '2020' : [ 2434,465,]
}
