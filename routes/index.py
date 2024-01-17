from flask import Flask, render_template, get_flashed_messages,url_for, Blueprint

index_blueprint = Blueprint("index_blueprint", __name__)

@index_blueprint.route("/")
@index_blueprint.route("/index")
def index():
    return render_template("index.html")