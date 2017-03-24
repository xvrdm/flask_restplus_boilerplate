from flask import current_app, Blueprint, jsonify
from flask_restplus import Resource, Api

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(v1, version=1.0, title='API v1')

@api.route('/hello')
class HelloWorld(Resource):
   def get(self):
       return jsonify({'message': 'hello world'})
