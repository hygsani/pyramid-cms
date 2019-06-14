from config import c_route_paths

def init_routes(config):
    ### web's routes ###
    config.add_route('web.home.index', '/')

    ### admin's routes ###
    config.add_route('admin.login.index', c_route_paths['admin'])
    config.add_route('admin.login.do_login', c_route_paths['admin'] + '/do_login')

    config.add_route('admin.dashboard.index', c_route_paths['admin'] + '/dashboard')
