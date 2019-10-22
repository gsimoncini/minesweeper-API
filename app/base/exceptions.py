from app import app
import flask

class ValidationError(Exception):

    def __init__(self, errors=None, warnings=None):
        super(ValidationError, self).__init__("Validation errors")
        self.warnings = warnings if warnings else []
        self.errors = errors if errors else []


@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return flask.jsonify(e.__dict__), 400


@app.errorhandler(Exception)
def handle_service_error(e):
    return flask.jsonify(
        message='The server encountered an internal error and was unable to complete your request. Error Message: {}'
            .format(e)), 500