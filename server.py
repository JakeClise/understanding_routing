from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    return f"Hello {name.capitalize()}"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''
    for i in range(0, num):
        output += f"<h4>{word}<h4>"
    return output




if __name__ == ("__main__"):
    app.run(debug=True)