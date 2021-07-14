# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import dessert_choice_message, link_dessert, title, picture
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ["GET", "POST"])
def results():
    print(request.form["desserts"])
    user_choice = request.form["desserts"]
    message = dessert_choice_message(user_choice)
    dessert_link = link_dessert(user_choice)
    title_for_recipe = title(user_choice)
    dessert_image = picture(user_choice)
    return render_template("results.html", message = message, dessert_link = dessert_link, title_for_recipe = title_for_recipe, dessert_image = dessert_image)