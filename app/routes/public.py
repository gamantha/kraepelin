from flask import Blueprint, request, render_template
from ..controllers import public_controller
public_routes = Blueprint('public', __name__)

@public_routes.route('/test', methods=['GET'])
def execute_kraepelin_test():
    # generate random value n*n
    data = public_controller.index(request)
    return render_template('index.html', title='Home', data=data)
