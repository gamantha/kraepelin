from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from ..controllers import public_controller
from ..util.login_required import login_required

public_routes = Blueprint('public', __name__)

@public_routes.route('/', methods=['GET'])
def login_page():
    # get login page
    return render_template('login.html', title='Login')

@public_routes.route('/login', methods=['POST'])
def post_login():
    # post login information
    result = public_controller.get_user(request)
    if result is None:
        flash('email yang anda masukkan salah atau belum terdaftar.')
        return redirect(url_for('public.login_page'))
    elif result['quota'] <= 0:
        flash('kuota test anda habis, silahkan hubungi admin.')
        return redirect(url_for('public.login_page'))
    session['user_id'] = result['id']
    return redirect(url_for('public.execute_kraepelin_test'))

@public_routes.route('/test', methods=['GET'])
@login_required
def execute_kraepelin_test(*args, **kwargs):
    # generate random value n*n
    data = public_controller.index(request)
    return render_template('index.html', title='Home', data=data)

@public_routes.route('/assess', methods=['POST'])
@login_required
def assess_kraepelin_test(*args, **kwargs):
    # assess user kraepelin test result
    return public_controller.assess_result(request, kwargs['user_id'])

@public_routes.route('/assess_result/<id>', methods=['GET'])
@login_required
def assess_kraepelin_result(id, *args, **kwargs):
    # result page
    graph_data = public_controller.get_filled_answer(id)
    return render_template('result.html', title='Result', result_id=id, graph_data=graph_data)
