from bottle import run, route, template, request
from models import Upload
import bottle


# Configuration

bottle.TEMPLATE_PATH = './templates/'


# Routes

@route('/')
def index():
    uploads = Upload.select().where(private == False).get()[:100]
    return template('index', uploads=uploads)


@route('/api/upload')
def upload():
    pass


# Run app

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
