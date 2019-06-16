from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy import desc

from app import Session
from models.post import Post
from config import *

@view_config(route_name='admin.dashboard.index', renderer=c_view_paths['admin'] + 'dashboard/index.jinja2')
def index(request):
    session = Session()
    latest_posts = session.query(Post).order_by(desc(Post.created_at)).limit(5).all()

    return dict(status='ok', view_path=c_view_paths['admin'], latest_posts=latest_posts)


@view_config(route_name='admin.dashboard.do_logout')
def do_logout(request):
    return HTTPFound(location='/admin')