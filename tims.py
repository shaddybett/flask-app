from flask import Flask
from flask_restful import Api,Resource

app =Flask(__name__)
api = Api(app)

class homePage(Resource):
    def get():
        return {'data':'welcome'}
    
api.add_resource(homePage)

if __name__=='__main__':
    app.run(debug=True,port=5555)