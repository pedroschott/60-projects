from flask import Flask

def create_app():
    app = Flask(__name__, static_folder="static")
    app.config['SECRET_KEY'] = 'adnsajsdmoaismdaoisdmaoisdm'

    #Register the blueprints
    from .directory import directory

    app.register_blueprint(directory, url_prefix='/')

    return app