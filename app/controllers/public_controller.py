from ..util.http import Http
from .base_controller import BaseController
from app.services import kraepelin_service

class PublicController(BaseController):
    """
    Public route controller.
    """

    def index(self, request):
        """
        Index path of public routes
        Generate needed data for displaying on front page.
        """
        size = request.args.get('size')
        data = kraepelin_service.prepare_test_data(size.split('x') if size else ['10', '5'])
        return data
    
    def assess_result(self, request):
        """
        Assess result of user answers.
        """
        # extract data
        payload = request.json['payload'] if  'payload' in request.json else None
        if payload is None:
            return self.json_response({}, Http.UNPROCESSABLE_ENTITY)
        # calculate and store user result
        try:
            result = kraepelin_service.asess_test_data(request.json['payload'])
            return self.json_response(result, status_code=Http.CREATED)
        except Exception as e:
            print(e)
            return self.error_response(e, '/assess', Http.INTERNAL_SERVER_ERROR)

    def get_filled_answer(self, id):
        """
        Get array of result to be printed
        """
        if id is None:
            return id
        try:
            result = kraepelin_service.get_filled_answer(id)
            return result
        except Exception as e:
            print(e)
            return None
