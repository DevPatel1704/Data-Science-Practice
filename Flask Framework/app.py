from flask import Flask

'''
It creates an instance Of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''

### WSGI application
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to the flask. There is a change . There is another change"

@app.route("/index")
def index():
    return "welcome to the index page"

if __name__== "__main__":
    app.run(debug=True)
    
