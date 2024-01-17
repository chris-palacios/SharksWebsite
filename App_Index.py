from flask import Flask
from flask import get_flashed_messages, render_template, redirect, request, Blueprint,url_for
from routes.index import index_blueprint
from routes.aboutUs import aboutUs_blueprint
from routes.contact import contact_blueprint
from routes.cart import cart_blueprint
appIndex = Flask(__name__)

appIndex.register_blueprint(index_blueprint)
appIndex.register_blueprint(aboutUs_blueprint)
appIndex.register_blueprint(contact_blueprint)
appIndex.register_blueprint(cart_blueprint)



