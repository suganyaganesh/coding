from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return 'welcome to web page'

@app.route('/about')
def about():
    return'this about page is another page route'

@app.route('/blog')
def blog():
    return 'this blog page contain blogs'

@app.route('/blog/<blog_id>')
def blogpost(blog_id):
    return ' this is blog post number' + str(blog_id)

if __name__=='__main__':
    app.run()