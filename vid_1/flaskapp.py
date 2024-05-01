from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello this is home page</h1>'

  
#in python two routes can redirect to the same page as well
@app.route('/about')
def about():
    return '<h1>Hello this is about page</h1>'

if __name__ == '__main__':
    app.run(debug=True) 