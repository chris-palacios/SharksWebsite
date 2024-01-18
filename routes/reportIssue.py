from flask import Flask, render_template, get_flashed_messages,url_for, Blueprint

report_bug_blueprint = Blueprint("report_bug_blueprint", __name__)

@report_bug_blueprint.route("/reportIssue")
def reportBug():
    return render_template("reportIssue.html")


