"""Flask Application for Paws Rescue Center."""
from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")

def homepage():
    return render_template ("home.html")


@app.route("/About page")
def About_page():
    return render_template("about.html")
    
if __name__ == "__main__":
   
    app.run(debug=True)