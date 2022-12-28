from flask import Flask, render_template, jsonify
import csv
from distutils.log import debug 

app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f: 
    reader = csv.DictReader(f)
    laureates = list(reader)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/laureates/")
def laureate():
    return jsonify(laureates)

app.run(debug=True) 