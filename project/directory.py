from flask import Blueprint, render_template

directory = Blueprint('directory', __name__)

@directory.route('/')
def main_directory():
    return render_template('base.html')