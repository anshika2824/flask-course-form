from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("course.html")

@app.route("/one",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("f_data.html")
    if request.method == "POST":
        c_name = request.form["c_name"]
        id = request.form.get("id")
        return render_template("course.html",c_name=c_name,id=id)

app.run(debug=True)
    
