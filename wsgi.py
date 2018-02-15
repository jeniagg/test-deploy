from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()

# from flask import Flask
# application = Flask(__name__)

# @application.route("/")
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     application.run()