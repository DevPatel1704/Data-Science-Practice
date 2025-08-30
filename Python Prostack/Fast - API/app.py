from fastapi import FastAPI

# create fastAPI app
app = FastAPI()
print(type(app))
# develop API
'''
API Usage : Application root request 
URL : http://127.0.0.1:8000/
Mthod Type : GET
required Fields : None
Access Type : Public
'''
@app.get('/')
def indexpage():
    return {"message":"Index Page"}

'''
API Usage : Application About Page request 
URL : http://127.0.0.1:8000/about
Mthod Type : GET
required Fields : None
Access Type : Public
'''
@app.get('/about')
def aboutpage():
    return {"message" : "About Page"}


'''
API Usage : Application Contact Page request 
URL : http://127.0.0.1:8000/contact
Mthod Type : GET
required Fields : None
Access Type : Public
'''
@app.get('/contact')
def contactpage():
    return {"message" : "Contact Page"}


'''
API Usage : Application Login Page request 
URL : http://127.0.0.1:8000/login
Mthod Type : POST
required Fields : None
Access Type : Public
'''
@app.post('/login')
def loginpage():
    return {"message" : "Login Page"}