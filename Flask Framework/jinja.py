### Building URL dynamically
## Variable Rule
### Jinja 2 template engine
'''
{{ }} expression to print output in html
{%....%} conditions, for loops
{#....#} comments
'''


from flask import Flask, render_template, request

### WSGI application
app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>Welcome to the html tags</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # handle POST request here
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

##Variable rule : Restricting a parameter that it must be integer it is called variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>50:
        res="passed"
    else:
        res="failed"
        
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>50:
        res="passed"
    else:
        res="failed"
        
    exp={'score':score,"res":res}
    return render_template('result1.html',results=exp)

@app.route('/successif/<int:score>')
def successif(score):
    
    return render_template('result.html',results=score)

if __name__== "__main__":
    app.run(debug=True)
    
