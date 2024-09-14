# main.py

from flask import Flask

app = Flask('__name__')


@app.route("/")
def bmi():
    return "<h1> Welcome to BMI apps</h1>"


if __name__ == "__main__":
    app.run(debug=True)
