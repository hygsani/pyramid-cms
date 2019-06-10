from pyramid.response import Response
from pyramid.view import view_config
from config import *

@view_config(route_name='web.home.index', renderer=c_view_paths['web'] + 'home/index.jinja2')
def index(request):
	return dict(status='ok', view_path=c_view_paths['web'])
