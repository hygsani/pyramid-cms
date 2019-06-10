from wsgiref.simple_server import make_server
from pyramid.config import Configurator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from routes import init_routes
from includes import init_includes
from scans import init_scans

PORT = 6543

engine = create_engine('mysql://cms:123@localhost/cms', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

if __name__ == '__main__':
    with Configurator() as config:
        init_routes(config)
        init_includes(config)
        init_scans(config)

        app = config.make_wsgi_app()
        print('web server running on port %d' % PORT)

    server = make_server('0.0.0.0', PORT, app)
    server.serve_forever()
