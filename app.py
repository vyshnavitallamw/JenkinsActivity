from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return "<h2>Hello World- Docker flask deployment lab</h2><hr/>"
    return "hey this is a new change i committed"

app.run(host="0.0.0.0",port=5000)
