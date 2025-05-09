"""WHAT WE'VE DONE SO FAR"""
"""
1. Created a virtual enviroment with venv "python -m venv venv
    -This created a venv folder containing a copy of python and pip for this project
    -Note: pip is python's package instaler (for external libaries)
2. Activated the virtual enviroment with "./venv/Scripts/activate"
    -This should put (venv) at the front of the command line
3. Installed flask with "pip install flask"

4. Created templates in a templates folder to return html pages
5. Rendered the templates with render_templates()
6. Created a requirements.txt file that will let you or others easily install packages the app nedds
    - Created with: pip freeze > requirments.txt
    - Can be run with pip install -r requirements.txt
7. Added a .gitignore to make sure we don't commit out venv stuff
8. Created static folder to be used to server other local resources (css/js/images)
    -used url_for()
"""

#import the Flask class from the flask module
from flask import Flask, render_template # render_template loads HTML from /templates
import datetime

#Create an instance of the Flask app
app=Flask(__name__)

#Define a route for a home page
@app.route("/")
def home():
    #Return a simple string that is valid HML
    #return "<h1>Welcome to my Flask App!</h1>"
    #Return the home template
    return render_template("home.html")

@app.route("/time")
def time():
    #get the current time on the server
    now = datetime.datetime.now()
    #return f"<h2>Current Server Time: {now}</h2>"

    return render_template("time.html", current_time=now)

if __name__ == "__main__":
    # debug = True enables automatic reload on changes and better error messages
    app.run(debug=True)