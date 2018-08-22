from flask import Blueprint, request, render_template, redirect, url_for
from ..controllers import public_controller
public_routes = Blueprint('public', __name__)

@public_routes.route('/test', methods=['GET'])
def execute_kraepelin_test():
    # generate random value n*n
    data = public_controller.index(request)
    return render_template('index.html', title='Home', data=data)

@public_routes.route('/assess', methods=['POST'])
def assess_kraepelin_test():
    # assess user kraepelin test result
    return public_controller.assess_result(request)

@public_routes.route('/assess_result/<id>', methods=['GET'])
def assess_kraepelin_result(id):
    # result page
    graph_data = public_controller.get_filled_answer(id)
    return render_template('result.html', title='Result', result_id=id, graph_data=graph_data)
