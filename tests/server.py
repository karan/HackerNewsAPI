from time import sleep
from os import path
from multiprocessing import Process

from bottle import Bottle, route, run, template


PRESETS_DIR = path.join(path.dirname(__file__), 'presets')


def template_response(func):
    def wrapper(*args, **kwargs):
        filename = func(*args, **kwargs)
        with open(path.join(PRESETS_DIR, filename)) as f:
            content = f.read()
        return template(content)
    return wrapper


class HNApp(Bottle):

    def __init__(self, host='localhost', port=8000):
        super(HNApp, self).__init__()
        self.host = host
        self.port = port
        self.process = None

    def run(self):
        run(self, host=self.host, port=self.port, debug=False, quiet=True)

    def start(self):
        self.process = Process(target=self.run)
        self.process.start()
        sleep(1)

    def stop(self):
        self.process.terminate()
        self.process = None

    @property
    def url(self):
        return 'http://{}:{}'.format(self.host, self.port)

hn = HNApp()


@hn.route('/')
@template_response
def index(**kwargs):
    return 'index.html'


@hn.route('/newest')
@template_response
def newest(**kwargs):
    return 'newest.html'


@hn.route('/leaders')
@template_response
def leaders(**kwargs):
    return 'leaders.html'


@hn.route('/news2')
@template_response
def news2(**kwargs):
    return 'news2.html'


@hn.route('/best')
@template_response
def best(**kwargs):
    return 'best.html'


@hn.route('/item?id=6115341')
@template_response
def s_6115341(**kwargs):
    return '6115341.html'


@hn.route('/item?id=6374031')
@template_response
def s_6374031(**kwargs):
    return '6374031.html'


@hn.route('/item?id=7324236')
@template_response
def s_7324236(**kwargs):
    return '7324236.html'


@hn.route('/item?id=7404389')
@template_response
def s_7404389(**kwargs):
    return '7404389.html'


if __name__ == '__main__':
    hn.run()
