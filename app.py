from flask import Flask,request,redirect,render_template,url_for
app = Flask(__name__)

@app.route("/")
def interface():
    return render_template('auth.html')
