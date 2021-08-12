# os standard Python library
import os
import json 
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

#creating an instance instaling to an variable named app
#__name__ is a build-in Python variable
#Flesk needs this to know where to look fo templates and static files
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


#@app.route is a decorator("@"=pie-notation)
#a decorator is a way of wrapping funcions
# "/" browse to the root

@app.route("/")
def index():
    #return "Hello, World"
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    
    # # method 1
    # fp = open("data/company.json", "r")
    # data = json.load(fp)
    # fp.close()

    # # method 2
    # fp = open("data/company.json", "r")
    # json_data = fp.read()
    # data = json.loads(json_data)
    # fp.close()

    # method 3
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        #print("Hello! Is anybody there?") # for test1
        # print(request.form)# for test2
        #print(request.form.get("name"))# for test3
        #print(request.form["email"])# for test4
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
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