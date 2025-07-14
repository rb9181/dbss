from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/dbs",methods=["GET","POST"])
def idbs():
    return(render_template("dbs.html"))

@app.route("/main,methods=["GET","POST"])
def main():
    q = (request.form.get("q")

    # db
    return(render_template("main.html",r=pred))
           
if __name__ == "__main__":
    app.run()
