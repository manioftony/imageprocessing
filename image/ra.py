from flask import Flask, request, jsonify, abort, url_for, g, render_template, redirect


app = Flask(__name__)


@app.route('/')
def index():
    obj = 'rashmi here'
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
