from pathlib import Path

root_path = str(Path().resolve())

c_view_paths = {
    'web': '/views/web/',
    'admin': '/views/admin/'
}

c_route_paths = {
    'web': '/',
    'admin': '/admin'
}

c_report_paths = {
    'jasper': root_path + '/jasper',
    'pdf': root_path + '/jasper/pdf'
}