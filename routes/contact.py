from flask import Flask, render_template, get_flashed_messages,url_for, Blueprint

contact_blueprint = Blueprint("contact_blueprint", __name__)

@contact_blueprint.route("/contact")
def contact():
    return render_template("contact.html")