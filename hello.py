from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hi")
def hello():
    return "hi World!"

@app.route("/bye")
def hello():
    return "Bye World!"

if __name__ == "__main__":
    app.run()
