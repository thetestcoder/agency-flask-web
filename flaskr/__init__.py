import os

from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev"
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/blog')
    def blog():
        return render_template("blog.html")

    @app.route('/contact')
    def contact():
        return render_template("contact.html")

    @app.route('/about')
    def about():
        return render_template("about.html")

    @app.route('/portfolio')
    def portfolio():
        return render_template("portfolio.html")

    @app.route('/services')
    def services():
        return render_template("services.html")

    return app