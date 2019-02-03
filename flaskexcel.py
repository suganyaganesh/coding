#develped by - Suganya on 03/02/2019	
# this code will excecute in Python 3 version
# Import Flask module from flask
from flask import Flask

# default arguments for flask in web
app=Flask(__name__)

# this is route function which / used to route the function in browser
@app.route('/')
# this is home function for the web Url after route in browser
def home():  
 return 'hello world'   # while execution it will return the Hello world
# this is another routing function which execute on open excel 
@app.route('/excel')
def excel(): # this is another function
 import excelopen        #import excel open function in module
 excelopen.os.system('start openxlexam.xlsx')   # this is call module for exceution
 return 'hello this is excel'
 
if __name__=='__main__':
 app.run()  # call the default app function 
 