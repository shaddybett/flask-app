from flask import Flask
from flask_restful import Api,Resource

app =Flask(__name__)
api = Api(app)

class HomePage(Resource):
    def get(self):
        return {'data':'welcome'}
    
api.add_resource(HomePage,'/homepage')

if __name__=='__main__':
    app.run(debug=True,port=5555)