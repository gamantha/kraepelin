from datetime import datetime

from flask import Response, json


class BaseController:
    """
    Basic controller functionalities, will be extended
    by other specific controllers.
    """

    @staticmethod
    def json_response(data: dict, status_code: int = 200):
        return Response(json.dumps(data, indent=1), status=status_code, mimetype='application/json')

    @staticmethod
    def error_response(error: Exception, path: str, status_code: int = 500):
        data = {
            'timestamp': datetime.now().timestamp(),
            'status': status_code,
            'error': str(error),
            'exception': ((error.__module__ + '.') if hasattr(error, '__module__') else '') + type(error).__name__,
            'message': str(error),
            'path': path,
        }
        return Response(json.dumps(data, indent=1), status=status_code, mimetype='application/json')
