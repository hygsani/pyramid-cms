from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from app import Session
from models.post import Post
from config import *

@view_config(route_name='admin.post.index', renderer=c_view_paths['admin'] + 'posts/index.jinja2')
def index(request):
    session = Session()

    posts = session.query(Post).all()

    return dict(status='ok', view_path=c_view_paths['admin'], posts=posts)


@view_config(route_name='admin.post.add', renderer=c_view_paths['admin'] + 'posts/add.jinjda2')
def add(request):
    return dict(status='ok', view_path=c_view_paths['admin'])


@view_config(route_name='admin.post.edit', renderer=c_view_paths['admin'] + 'posts/edit.jinja2')
def edit(request):
    return dict(status='ok', view_path=c_view_paths['admin'])


@view_config(route_name='admin.post.delete', renderer=c_view_paths['admin'] + 'post/sdelete.jinja2')
def delete(request):
    return dict(status='ok', view_path=c_view_paths['admin'])