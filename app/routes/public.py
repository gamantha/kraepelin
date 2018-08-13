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

@public_routes.route('/assess_result', methods=['GET'])
def assess_kraepelin_result():
    # result page
    return render_template('result.html', title='Result')
