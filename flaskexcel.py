from flask import Flask


app=Flask(__name__)

@app.route('/')
def home():
 return 'hello world'
@app.route('/excel')
def excel():
 import test
 test.os.system('start bar.xlsx')
 return 'hello this is excel'
 
if __name__=='__main__':
 app.run()
 