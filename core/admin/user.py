from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from app import Session
from models.user import User
from config import *

@view_config(route_name='admin.user.edit', renderer=c_view_paths['admin'] + 'users/edit.jinja2')
def edit(request):
    pass


