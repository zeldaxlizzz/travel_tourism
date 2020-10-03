from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/tourist')
def contact():
   return render_template("tourist.html")

@app.route('/dance')
def dance():
   return render_template("dance.html")

@app.route('/feedback')
def feedback():
   return render_template("feedback.html")

@app.route('/festival')
def festival():
   return render_template("festival.html")

@app.route('/submit')
def submit():
   return render_template("submit.html")

@app.route('/food')
def food():
   return render_template("food.html")