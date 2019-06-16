from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from app import Session
from models.user import User
from config import *

@view_config(route_name='admin.user.edit', renderer=c_view_paths['admin'] + 'users/edit.jinja2')
def edit(request):
    session = Session()
    user = session.query(User).get(request.session['user_id'])

    if user == None:
        return HTTPFound(location='/admin/dashboard')

    return dict(status='ok', view_path=c_view_paths['admin'], user=user)


@view_config(route_name='admin.user.do_edit')
def do_edit(request):
    user_id = request.matchdict['id']

    if request.params.get('password') == request.params.get('confirm_password'):
        session = Session()
        user = session.query(User).get(user_id)

        user.name = request.params.get('name')
        user.email = request.params.get('email')
        user.password = request.params.get('password')

        session.add(user)
        session.commit()

        request.session['name'] = request.params.get('name')
        request.session['email'] = request.params.get('email')
    else:
        return HTTPFound(location='/admin/user/%s/edit' % user_id)

    return HTTPFound(location='/admin/dashboard')
