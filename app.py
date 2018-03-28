from flask import Flask, render_template
from livereload import Server, shell


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve()
