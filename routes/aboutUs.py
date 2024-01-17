from flask import Flask, render_template, get_flashed_messages,url_for, Blueprint

aboutUs_blueprint = Blueprint("aboutUs_blueprint", __name__)

@aboutUs_blueprint.route("/aboutus")
def aboutUs():
    return render_template("aboutUs.html")