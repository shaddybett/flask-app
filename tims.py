from flask import Flask
from flask_restful import Api,Resource

app =Flask(__name__)
api = Api(app)

class HomePage(Resource):
    def get(self,name,age):
        return {'name':'tim','age':20}
    
api.add_resource(HomePage,'/homepage/<string:name>/<int:age>')

if __name__=='__main__':
    app.run(debug=True,port=5555)