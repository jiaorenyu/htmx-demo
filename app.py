from re import escape
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/demo/")
def demo():
    return render_template('demo.html')


@app.route("/text/", methods=['POST'])
def text():
    print(request.form)
    text = escape(request.form["entext"])
    word_list = text.split()
    word_freq = {}
    for word in word_list:
        freq = word_freq[word] if word in word_freq else 0
        word_freq[word] = freq + 1

    return render_template('word_list.html', word_freq=word_freq)

@app.route("/")
def index():
    return render_template('index.html')


