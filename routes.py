from config import c_route_paths

def init_routes(config):
    ### web's routes ###
    config.add_route('web.home.index', '/')

    ### admin's routes ###
    config.add_route('admin.login.index', c_route_paths['admin'])
    config.add_route('admin.login.do_login', c_route_paths['admin'] + '/do_login')

    config.add_route('admin.dashboard.index', c_route_paths['admin'] + '/dashboard')
    config.add_route('admin.dashboard.do_logout', c_route_paths['admin'] + '/dashboard/do_logout')

    config.add_route('admin.post.index', c_route_paths['admin'] + '/post')
    config.add_route('admin.post.add', c_route_paths['admin'] + '/post/add')
    config.add_route('admin.post.do_add', c_route_paths['admin'] + '/post/do_add')
    config.add_route('admin.post.edit', c_route_paths['admin'] + '/post/{id}/edit')
    config.add_route('admin.post.do_edit', c_route_paths['admin'] + '/post/{id}/do_edit')
    config.add_route('admin.post.delete', c_route_paths['admin'] + '/post/{id}/delete')
    config.add_route('admin.post.do_delete', c_route_paths['admin'] + '/post/{id}/do_delete')
