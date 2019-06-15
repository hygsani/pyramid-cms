from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from datetime import datetime

from app import Session
from models.post import Post
from config import *

@view_config(route_name='admin.post.index', renderer=c_view_paths['admin'] + 'posts/index.jinja2')
def index(request):
    session = Session()
    posts = session.query(Post).all()

    return dict(status='ok', view_path=c_view_paths['admin'], posts=posts)


@view_config(route_name='admin.post.add', renderer=c_view_paths['admin'] + 'posts/add.jinja2')
def add(request):
    return dict(status='ok', view_path=c_view_paths['admin'])


@view_config(route_name='admin.post.edit', renderer=c_view_paths['admin'] + 'posts/edit.jinja2')
def edit(request):
    session = Session()
    post_id = request.matchdict['id']
    post = session.query(Post).get(post_id)

    if post == None:
        return HTTPFound(location='/admin/post')

    return dict(status='ok', view_path=c_view_paths['admin'], post=post)


@view_config(route_name='admin.post.delete', renderer=c_view_paths['admin'] + 'post/delete.jinja2')
def delete(request):
    return dict(status='ok', view_path=c_view_paths['admin'])


@view_config(route_name='admin.post.do_add')
def do_add(request):
    session = Session()
    title = request.params.get('title')
    content = request.params.get('content')
    is_published = request.params.get('is_published')

    post = Post(
        title=title,
        content=content,
        is_published=is_published,
        created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        created_by=1
    )

    session.add(post)
    session.commit()

    return HTTPFound(location='/admin/post')


@view_config(route_name='admin.post.do_edit')
def do_edit(request):
    session = Session()
    post_id = request.matchdict['id']
    title = request.params.get('title')
    content = request.params.get('content')
    is_published = request.params.get('is_published')
    post = session.query(Post).get(post_id)

    post.title = title
    post.content = content
    post.is_published = is_published
    post.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    post.updated_by = 1

    session.add(post)
    session.commit()

    return HTTPFound(location='/admin/post')