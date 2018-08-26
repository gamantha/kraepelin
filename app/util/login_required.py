import time
from flask import redirect, url_for, session, flash
from functools import wraps
import logging

log = logging.getLogger(__name__)


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get('user_id') is None:
            flash('Anda harus login terlebih dahulu.')
            return redirect(url_for('public.login_page'))
        kwargs['user_id'] = session.get('user_id')
        return f(*args, **kwargs)
    return decorated
