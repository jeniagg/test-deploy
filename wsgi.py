from flask import Flask
# from flask_restful import Resource, Api

app = Flask(__name__)
# api = Api(app)


class HelloWorld:
    @app.route('/', methods=['GET'])
    def get(self):
        return {'new': 'sm'}
    
    @app.route('/s/smth', methods=['GET'])
    def getNew(self):
        return {'hesmllo': 'new'}

# api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()

# from flask import Flask
# application = Flask(__name__)

# @application.route("/")
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     application.run()