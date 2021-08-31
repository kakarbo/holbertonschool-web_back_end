#!/usr/bin/env python3
"""setup a basic Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """an index.html template
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
