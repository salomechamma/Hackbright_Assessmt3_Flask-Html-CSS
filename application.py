from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
@app.route("/application-form")
def show_application_form():
    """Show application form page."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def confirmation_application():
    """Confirm submission of application."""

    fname = request.form.get("fname").title()
    lname = request.form.get("lname").title()
    salary = request.form.get("salary")
    title = request.form.get("title")

    return render_template("application-response.html", first_name=fname, last_name=lname, 
        salary=salary, job_title=title)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

