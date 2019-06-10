from pyramid.response import Response
from pyramid.view import view_config
from config import *

@view_config(route_name='admin.login.index', renderer=c_view_paths['admin'] + 'login/index.jinja2')
def index(request):
    return dict(status='ok', view_path=c_view_paths['admin'])