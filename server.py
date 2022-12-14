from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/flask')
def say_flask():
    return "Hi Flask!"

@app.route('/say/michael')
def say_michael():
    return "Hi Michael!"

@app.route('/say/john')
def say_john():
    return "Hi John!"

@app.route('/repeat/35/hello')
def repeat_hello():
    return "hello " * 35

@app.route('/bye/80')
def repeat_bye():
    return "bye " * 80
@app.route('/dog/99')
def repeat_dog():
    return "dog " * 99
    



if __name__ == ("__main__"):
    app.run(debug=True)