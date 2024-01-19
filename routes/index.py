from flask import Flask, render_template, get_flashed_messages,url_for, Blueprint
import json

index_blueprint = Blueprint("index_blueprint", __name__)

@index_blueprint.route("/")
@index_blueprint.route("/index")
def index():
    json_file= "C:\\Users\\links\\Documents\\GitHub\\SharksWebsite\\data\\articles.json"
    with open(json_file) as json_data:
        article = json.load(json_data)
        
    return render_template("index.html", article=article)