from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from app import Session
from models.user import User
from config import *

@view_config(route_name='admin.login.index', renderer=c_view_paths['admin'] + 'login/index.jinja2')
def index(request):
    return dict(status='ok', view_path=c_view_paths['admin'])


@view_config(route_name='admin.login.do_login')
def do_login(request):
    session = Session()

    email = request.params.get('email')
    password = request.params.get('password')

    user = session.query(User).filter(User.email == email, User.password == password).first()

    if user == None:
        return HTTPFound(location='/admin')

    app_session = request.session
    app_session['user_id'] = user.user_id
    app_session['email'] = user.email
    app_session['name'] = user.name

    return HTTPFound(location='/admin/dashboard')