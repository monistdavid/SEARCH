from flask import Flask, render_template, request, Blueprint, flash, redirect, session, url_for


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, template_folder='templates')

    # auth the blueprint
    from view import all_bp
    for bp in all_bp:
        app.register_blueprint(bp)
    return app


application = create_app()

if __name__ == "__main__":
    application.run(port=8000, use_reloader=True)
