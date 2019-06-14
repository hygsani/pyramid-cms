from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from app import Session
from config import *

@view_config(route_name='admin.dashboard.index', renderer=c_view_paths['admin'] + 'dashboard/index.jinja2')
def index(request):
    return dict(status='ok', view_path=c_view_paths['admin'])


@view_config(route_name='admin.dashboard.do_logout')
def do_logout(request):
    return HTTPFound(location='/admin')