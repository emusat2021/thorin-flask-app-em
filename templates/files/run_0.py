# os standard Python library
import os
import json 
from flask import Flask, render_template

#creating an instance instaling to an variable named app
#__name__ is a build-in Python variable
#Flesk needs this to know where to look fo templates and static files
app = Flask(__name__)


#@app.route is a decorator("@"=pie-notation)
#a decorator is a way of wrapping funcions
# "/" browse to the root

@app.route("/")
def index():
    #return "Hello, World"
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3])


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")



#__main__ is the name of the default module in Python
#'IP' environment variable if it exists, but set a default value if it's not found
#PORT casting it as an integer, and I will set that default to "5000", 
# which is a common port used by Flask.
#"debug=True" will allows to debug much easier
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)