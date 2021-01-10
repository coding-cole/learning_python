from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return "Homepage here"

if __name__=="__main__":
    app.run(debug=True)