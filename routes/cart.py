from flask import Flask, render_template, get_flashed_messages,url_for, Blueprint

cart_blueprint = Blueprint("cart_blueprint", __name__)

@cart_blueprint.route("/cart")
def cart():
    return render_template("cart.html")