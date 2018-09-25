from flask import Flask, Blueprint
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from bitly import Bitly
import pdb

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

blueprint = Blueprint('api', __name__, url_prefix='/api/bfg')
api = Api(blueprint, version='v0.1', title='BFG',  description='Documentation of BFG apis')

app.register_blueprint(blueprint)

api.namespaces.clear() # clear default namespace.

shorten_url_ns = api.namespace('shorten', description='shorten URL for long URL')

shorten_url_model = api.model('shorten_url', {
    'tinyurl': fields.String(required=True, description='shorten url')
})

@shorten_url_ns.route('/<string:longUrl>')
@shorten_url_ns.param('longUrl', 'Long Url')
class ShortenUrl(Resource):
    @shorten_url_ns.marshal_with(shorten_url_model, code=201)
    def get(self, longUrl):
        ''' Get shorten Url'''
        pdb.set_trace()
        shortUrl = bitlyOb.getShortenUrl(longUrl)
        return shortUrl

if __name__ == '__main__':
    bitlyOb = Bitly();
    app.run(host='0.0.0.0', port=8080, debug=True)
	   
