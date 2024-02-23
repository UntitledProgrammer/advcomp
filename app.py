from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World</h1>"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
