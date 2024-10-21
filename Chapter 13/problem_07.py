'''
Question:- . Explore the ‘Flask’ module and create a web server 
using Flask & Python.
(pip install flask)
'''

# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

app.run() #this will run the application on execution, we can also find other ways to run it in it's documentation in google