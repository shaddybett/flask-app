from flask import Flask
from flask_restful import Api,Resource

app =Flask(__name__)
api = Api(app)

class HomePage(Resource):
    def get(self,name):
        return {'name':'tim'}
    
api.add_resource(HomePage,'/homepage/<string:name>')

if __name__=='__main__':
    app.run(debug=True,port=5555)