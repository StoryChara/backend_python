from flask import Blueprint, render_template

error_blueprint = Blueprint("errors", __name__)

@error_blueprint.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403

@error_blueprint.errorhandler(404)
def forbidden_error(error):
    return render_template('404.html'), 404