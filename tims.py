from flask import Flask
from flask_restful import Api,Resource

app =Flask(__name__)
api = Api(app)

videos = {}

class Video(Resource):
    def put(self,video_id):
        return video_id
    
api.add_resource(Video,'/video')

if __name__=='__main__':
    app.run(debug=True,port=5555)