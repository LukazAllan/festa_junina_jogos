__author__ = "LukazAllan"
__version__ = "0.1.0"

from flask import Flask, render_template, request, redirect, url_for
from gerar_fase import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

