from app.services import kraepelin_service

class PublicController():
    """
    Public route controller.
    """

    def index(self, request):
        """
        Index path of public routes
        Generate needed data for displaying on front page.
        """
        size = request.args.get('size')
        data = kraepelin_service.prepare_test_data(size.split('x') if size else ['5', '5'])
        return data
