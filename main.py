from flask import Flask , request , redirect , render_template
from tinydb import TinyDB , Query
import random


app = Flask(__name__)
db = TinyDB("data.json")
Todo = Query()


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/create",methods=["GET","POST"])
def create():
  data = request.values
  url = data.get("url")
  code = random.randint(10000,99999)
  text = "abcdefghijklmnopqrstuvwxyz"
  new_url = "".join([random.choice(text) for i in range(6)])
  form = {
    "code":code,
    "url":url,
    "new_url":new_url
  }
  db.insert(form)
  print(form)
  return str(f"new url : localhost/link/{new_url}")


@app.route("/link/<url>")
def linker(url):
  link = db.get(Todo.new_url==url).get("url")
  return redirect("http://"+link)

app.run(debug=True , host="0.0.0.0", port=7777)